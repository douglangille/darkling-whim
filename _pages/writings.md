---
layout: archive
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

{% assign category_posts = site.categories['writings'] %}
{% assign tags_array = category_posts | map: 'tags' | join: ',' | split: ',' | uniq | sort %}

<ul class="taxonomy__index">
  {% for tag_name in tags_array %}
    {% if tag_name != "" %}
    <li>
      <a href="{{ site.baseurl }}/{{ tag_name | slugify }}/">
        <strong>{{ tag_name }}</strong>
      </a>
    </li>
    {% endif %}
  {% endfor %}
</ul>

<p class="notice">Prefer to read a series from the beginning? <a href="/haleys-war/">Haley's War</a> is an unfinished chaotic fever dream, but it's a helluva ride.</p>

<div class="entries-{{ page.entries_layout }}">
{% for post in paginator.posts %}
  {% include archive-single.html type=page.entries_layout %}
{% endfor %}
</div>

{% include paginator.html %}
