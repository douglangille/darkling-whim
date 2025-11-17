// QuickAdd — Copy active note + its one-level internal linked notes to clipboard
// Paste this into a QuickAdd "User Script" choice. Uses Obsidian's app API.
(async () => {
  try {
    const file = app.workspace.getActiveFile();
    if (!file) {
      new Notice("QuickAdd: no active file");
      return;
    }
    const vault = app.vault;
    const sourcePath = file.path;
    const sourceText = await vault.read(file);

    // Find wiki-links and embedded wiki-links like [[Note]] [[Note#heading]] [[alias|Note]] and ![[Note]]
    // Capture the leftmost part before any # or | so we resolve the base note name.
    const linkRegex = /\[!?\[([^\]\]]+)\]\]/g;
    const found = new Set();
    let m;
    while ((m = linkRegex.exec(sourceText)) !== null) {
      // m[1] can be "alias|Target" or "Target#Heading" etc.
      let target = m[1].split("|").pop().split("#")[0].trim();
      if (target) found.add(target);
    }

    // Resolve each link to a TFile and read it (skip if same as source)
    const linkedFiles = [];
    for (const linkName of found) {
      const dest = app.metadataCache.getFirstLinkpathDest(linkName, sourcePath);
      if (dest && dest.path !== sourcePath) {
        try {
          const text = await vault.read(dest);
          linkedFiles.push({ path: dest.path, name: dest.basename, text });
        } catch (e) {
          console.error("Failed reading", dest.path, e);
        }
      }
    }

    // Build clipboard text: source first, then each linked note with a separator header
    let out = `--- ${file.basename} (path: ${file.path}) ---\n\n${sourceText}\n`;
    for (const lf of linkedFiles) {
      out += `\n\n--- ${lf.name} (path: ${lf.path}) ---\n\n${lf.text}\n`;
    }

    // Copy to clipboard
    // On desktop Obsidian navigator.clipboard.writeText should work.
    await navigator.clipboard.writeText(out);

    new Notice(`Copied "${file.basename}" + ${linkedFiles.length} linked note(s) to clipboard.`);
  } catch (err) {
    console.error(err);
    new Notice("QuickAdd: error copying notes — see console");
  }
})();