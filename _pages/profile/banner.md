---
layout: default
permalink: /banner/
title: "Banner"
sitemap: false
robots: noindex
---
<style>
  /* One-off 1500x500 banner. Screenshot the .banner element. Not linked from anywhere. */
  .skip, .masthead, .footer { display: none; }
  html, body { margin: 0; background: var(--bg); }
  main { padding: 0; }
  .banner { position: relative; width: 1500px; height: 500px; overflow: hidden; background: var(--bg); color: var(--text); }
  .banner svg { position: absolute; inset: 0; width: 100%; height: 100%; }
  .banner__mark { position: absolute; left: 0; right: 0; top: 50%; transform: translateY(-50%); margin: 0; text-align: center; font-family: var(--font-mark); font-weight: 400; font-size: 150px; line-height: 1; letter-spacing: .02em; white-space: nowrap; color: var(--text); }
</style>
<div class="banner" id="banner">
  <svg viewBox="0 0 1500 500" aria-hidden="true" fill="none">
    <!-- concentric rings, off-centre moon -->
    <g stroke="var(--line)" stroke-width="2">
      <circle cx="750" cy="250" r="120"/>
      <circle cx="750" cy="250" r="190"/>
      <circle cx="750" cy="250" r="260"/>
      <circle cx="750" cy="250" r="330"/>
      <circle cx="750" cy="250" r="400"/>
    </g>
    <!-- horizon and radial ticks -->
    <path d="M0 250H1500" stroke="var(--line)" stroke-width="2"/>
    <g stroke="var(--accent)" stroke-width="3">
      <path d="M0 250H300 M1200 250H1500"/>
      <path d="M300 230V270 M1200 230V270"/>
    </g>
    <!-- crescent, upper left and lower right -->
    <path d="M170 90a70 70 0 1 0 0 140a56 56 0 1 1 0-140z" fill="var(--accent)" opacity=".9"/>
    <circle cx="1330" cy="410" r="14" fill="var(--accent)"/>
    <circle cx="1390" cy="370" r="6" fill="var(--accent)"/>
    <circle cx="1280" cy="450" r="4" fill="var(--accent)"/>
  </svg>
  <h1 class="banner__mark">{{ site.title }}</h1>
</div>
