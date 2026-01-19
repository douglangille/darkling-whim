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

{% assign writings_posts = site.categories['writings'] %}
{% assign all_tags = "" | split: "" %}
{% for post in writings_posts %}
  {% for tag in post.tags %}
    {% unless all_tags contains tag %}
      {% assign all_tags = all_tags | push: tag %}
    {% endunless %}
  {% endfor %}
{% endfor %}
{% assign all_tags = all_tags | sort %}

{% if all_tags.size > 0 %}
<ul class="taxonomy__index">
  {% for tag in all_tags %}
    <li>
      <a href="{{ site.baseurl }}/{{ tag | slugify }}/">
        <strong>{{ tag }}</strong>
      </a>
    </li>
  {% endfor %}
</ul>
{% endif %}

<p class="notice">Prefer to read a series from the beginning? <a href="/haleys-war/">Haley's War</a> is an unfinished chaotic fever dream, but it's a helluva ride.</p>
