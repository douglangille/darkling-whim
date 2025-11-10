ok..<%*
/**
 * Send to GPT (flatten-2 with titles) — copy-only
 * - Recursively expands ![[Note]], [[Note]], [[Note#Heading]], [[Note|Alias]]
 * - Depth limit: 2 (configurable via MAX_DEPTH)
 * - Injects normalized titles per depth:
 *     depth 0 -> "## {Title}"
 *     depth 1 -> "### {Title}"
 *     depth 2 -> "#### {Title}"
 * - Strips YAML frontmatter + the first body H1 of each expanded note
 * - Uses frontmatter 'title' -> H1 -> filename to derive Title
 * - Tracks note+section visits to prevent cycles
 * - Works on selection or whole note; inserts nothing (tR = "")
 */

const MAX_DEPTH = 2; // <- change to 1 or 2 (recommended)
const HEADING_AT_DEPTH = ["## ", "### ", "#### "]; // depth 0/1/2 headings

function stripFrontmatter(md){ return md.replace(/^---[\s\S]*?---\n/, ''); }
function splitFrontmatter(md){ const m = md.match(/^---\n([\s\S]*?)\n---\n?/); return m ? { fm:m[1], body: md.slice(m[0].length) } : { fm:null, body: md }; }
function getBasename(path){ return path.split('/').pop().replace(/\.md$/,''); }

function parseTitleAndBody(md, fallbackTitle) {
  const { fm, body } = splitFrontmatter(md);
  let titleFromFM = null;
  if (fm) {
    const t = fm.match(/\btitle\s*:\s*(.+)\n?/i);
    if (t) titleFromFM = t[1].trim().replace(/^["']|["']$/g,'');
  }
  // extract and remove first H1
  const h1m = body.match(/^\#\s+(.+)\s*$/m);
  let h1 = h1m ? h1m[1].trim() : null;
  let cleanBody = body;
  if (h1m) {
    const idx = h1m.index, line = h1m[0];
    cleanBody = body.slice(0, idx) + body.slice(idx + line.length).replace(/^\s*\n/, '');
  }
  const title = (titleFromFM || h1 || fallbackTitle || "Untitled").trim();
  return { title, body: cleanBody.trim() };
}

function extractHeadingBlock(md, heading) {
  if (!heading) return md;
  const esc = heading.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  const re = new RegExp(`^#{1,6}\\s+${esc}\\s*$`, 'mi');
  const start = md.search(re);
  if (start < 0) return null;
  const after = md.slice(start);
  const next = after.slice(1).search(/^\#{1,6}\s+/m);
  return next >= 0 ? after.slice(0, next + 1) : after;
}

function buildAliasIndex() {
  const idx = new Map();
  for (const tf of app.vault.getMarkdownFiles()) {
    const cache = app.metadataCache.getCache(tf.path);
    const fm = cache?.frontmatter;
    if (!fm) continue;
    let aliases = fm.aliases ?? fm.Aliases ?? fm.alias ?? [];
    if (typeof aliases === 'string') aliases = [aliases];
    if (Array.isArray(aliases)) for (const a of aliases) if (a && a.trim()) idx.set(a.trim(), tf);
    if (typeof fm.title === 'string' && fm.title.trim()) idx.set(fm.title.trim(), tf);
  }
  return idx;
}

function resolveTarget(raw, basePath, aliasIdx) {
  // [[Note|Display]], [[Note#Heading]], [[Alias]], [[Alias#Heading]]
  let target = raw;
  const pipe = target.indexOf('|');
  if (pipe !== -1) target = target.slice(0, pipe);
  let section = null;
  const hash = target.indexOf('#');
  if (hash !== -1) { section = target.slice(hash+1).trim(); target = target.slice(0, hash).trim(); }
  target = target.trim();
  let tfile = app.metadataCache.getFirstLinkpathDest(target, basePath);
  if (!tfile && target) tfile = aliasIdx.get(target) || null;
  return { tfile, section };
}

async function readMd(tfile) {
  if (!tfile || tfile.extension !== 'md') return null;
  return stripFrontmatter(await app.vault.read(tfile));
}

async function expandLinks(text, basePath, aliasIdx, depth, visits, stats, unresolved) {
  if (depth > MAX_DEPTH) { stats.depthLimited = true; return text; }

  const re = /!?\[\[([^\]]+)\]\]/g;
  let out = '', last = 0, m;

  while ((m = re.exec(text)) !== null) {
    out += text.slice(last, m.index);
    const raw = m[0], inside = m[1].trim();

    const { tfile, section } = resolveTarget(inside, basePath, aliasIdx);
    const md = await readMd(tfile);

    if (md !== null) {
      const key = tfile.path + '|' + (section || '');
      if (visits.has(key)) {
        out += raw; // guard against cycles
      } else {
        visits.add(key);
        let chunk = section ? (extractHeadingBlock(md, section) || md) : md;

        // Normalize title & strip internal H1
        const fallbackTitle = section ? `${getBasename(tfile.path)} – ${section}` : getBasename(tfile.path);
        const { title, body } = parseTitleAndBody(chunk, fallbackTitle);

        // Recurse into body
        stats.expanded++;
        const inner = await expandLinks(body, tfile.path, aliasIdx, depth+1, visits, stats, unresolved);

        // Inject heading for this expansion based on depth
        const headingPrefix = HEADING_AT_DEPTH[Math.min(depth, HEADING_AT_DEPTH.length-1)];
        out += (headingPrefix ? headingPrefix + title + "\n\n" : "") + inner;

        visits.delete(key);
      }
    } else {
      unresolved.push(inside);
      out += raw; // unresolved left as-is
    }
    last = re.lastIndex;
  }
  out += text.slice(last);
  return out;
}

try {
  const file = app.workspace.getActiveFile();
  if (!file) { new Notice("No active file"); tR=""; return; }

  const ed = app.workspace.activeEditor?.editor;
  let src = (ed && typeof ed.getSelection === 'function') ? ed.getSelection() : '';
  if (!src) src = await app.vault.read(file);
  src = stripFrontmatter(src);

  const aliasIdx = buildAliasIndex();
  const stats = { expanded: 0, depthLimited: false };
  const unresolved = [];
  const visits = new Set();

  const payload = (await expandLinks(src, file.path, aliasIdx, 0, visits, stats, unresolved)).trim();

  // Copy to clipboard (navigator first, Electron fallback)
  let copied = false;
  try { if (navigator?.clipboard?.writeText) { await navigator.clipboard.writeText(payload); copied = true; } } catch {}
  if (!copied) { try { const { clipboard } = window.require('electron'); clipboard.writeText(payload); copied = true; } catch {} }
  if (!copied) { new Notice("Clipboard unavailable; copy manually.", 6000); tR=""; return; }

  let msg = `Copied (${payload.length.toLocaleString()} chars, ${stats.expanded} expansions`;
  msg += stats.depthLimited ? `, depth-limited @ ${MAX_DEPTH}` : ``;
  msg += `)`;
  if (unresolved.length) msg += ` • Unresolved: ${[...new Set(unresolved)].slice(0,5).join(", ")}${unresolved.length>5?"…":""}`;
  new Notice(msg, 6000);

} catch (e) {
  new Notice("Templater error: " + (e?.message ?? e), 8000);
}
tR = "";
%>