#!/usr/bin/env node

const { AtpAgent } = require(”@atproto/api”);
const fetch = require(“node-fetch”);
const { parseStringPromise } = require(“xml2js”);

const FEED_URL = “https://douglangille.ca/feed.xml”;
const BLUESKY_HANDLE = process.env.BLUESKY_HANDLE;
const BLUESKY_PASSWORD = process.env.BLUESKY_PASSWORD;

if (!BLUESKY_HANDLE || !BLUESKY_PASSWORD) {
console.error(“Missing BLUESKY_HANDLE or BLUESKY_PASSWORD env vars”);
process.exit(1);
}

async function fetchFeed() {
const response = await fetch(FEED_URL);
const xml = await response.text();
const parsed = await parseStringPromise(xml, {
explicitArray: true,
mergeAttrs: false,
});

const items = parsed.rss.channel[0].item;
if (!items || items.length === 0) {
throw new Error(“No items in feed”);
}

const latest = items[0];

let imageUrl = null;
if (latest[“media:content”] && latest[“media:content”][0]) {
imageUrl = latest[“media:content”][0].$.url;
} else if (latest.enclosure && latest.enclosure[0]) {
imageUrl = latest.enclosure[0].$.url;
}

return {
title: latest.title[0],
link: latest.link[0],
excerpt: decodeHtmlEntities(latest.description[0]),
pubDate: latest.pubDate[0],
imageUrl: imageUrl,
tags: latest.category
? (Array.isArray(latest.category)
? latest.category
: [latest.category])
: [],
};
}

function decodeHtmlEntities(text) {
return text
.replace(/'/g, “’”)
.replace(/"/g, ‘”’)
.replace(/&/g, “&”)
.replace(/</g, “<”)
.replace(/>/g, “>”);
}

async function postToBluesky(story) {
const agent = new AtpAgent({
service: “https://bsky.social”,
});

await agent.login({
identifier: BLUESKY_HANDLE,
password: BLUESKY_PASSWORD,
});

const bskyTags = story.tags.map((tag) =>
tag === “flash” ? “flashfiction” : tag
);
const tagString = bskyTags.length
? bskyTags.map((tag) => `#${tag}`).join(” “)
: “.”;

const record = {
text: tagString,
createdAt: new Date().toISOString(),
facets: [],
embed: null,
};

record.embed = {
$type: “app.bsky.embed.external”,
external: {
uri: story.link,
title: story.title,
description: story.excerpt,
thumb: story.imageUrl
? await uploadImage(agent, story.imageUrl)
: null,
},
};

const response = await agent.post(record);
console.log(`Posted to Bluesky: ${response.uri}`);
}

async function uploadImage(agent, imageUrl) {
try {
const response = await fetch(imageUrl);
const buffer = await response.buffer();

```
const uploaded = await agent.uploadBlob(buffer, {
  encoding: "image/jpeg",
});

return uploaded.data.blob;
```

} catch (error) {
console.warn(“Failed to upload image:”, error.message);
return null;
}
}

async function main() {
try {
console.log(“Fetching latest story from feed…”);
const story = await fetchFeed();
console.log(`Found: "${story.title}"`);

```
console.log("Posting to Bluesky...");
await postToBluesky(story);

console.log("Done.");
```

} catch (error) {
console.error(“Error:”, error.message);
process.exit(1);
}
}

main();
