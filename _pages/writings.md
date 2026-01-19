---
layout: archive-writings
title: Stories & Poems
permalink: /writings/
entries_layout: grid
search: false
classes: wide
author_profile: true
pagination:
    enabled: true
    category: writings
---

<ul class="taxonomy__index">
{% for tag in site.tags %}
  {% assign tag_posts = tag[1] | where_exp: "post", "post.categories contains 'writings'" %}
  {% if tag_posts.size > 0 %}
  <li>
    <a href="/{{ tag[0] | slugify }}/">
      <strong>{{ tag[0] }}</strong> <span class="taxonomy__count">{{ tag_posts.size }}</span>
    </a>
  </li>
  {% endif %}
{% endfor %}
</ul>

<p class="notice">Prefer to read a series from the beginning? <a href="/haleys-war/">Haley's War</a> is an unfinished chaotic fever dream, but it's a helluva ride.</p>
