---
layout: archive-writings
title: Stories & Poems
permalink: /writings/
taxonomy: writings
entries_layout: grid
search: false
classes: wide
author_profile: true
pagination:
    enabled: true
    category: writings
---

{% assign alltags = site.categories['writings'] | sort %}
{% assign grouptag = alltags | map: 'tags' | join: ',' | split: ',' | group_by: tag | sort: 'name' %}
<ul class="taxonomy__index">
  {% for tag in grouptag %}
    <li>
      <a href="{{ site.baseurl }}/{{ tag.name | slugify }}/">
        <strong>{{ tag.name }}</strong> <span class="taxonomy__count">{{ tag.size }}</span>
      </a>
    </li>
  {% endfor %}
</ul>

<p class="notice">Prefer to read a series from the beginning? <a href="/haleys-war/">Haley's War</a> is an unfinished chaotic fever dream, but it's a helluva ride.</p>
