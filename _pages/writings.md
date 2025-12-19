---
title: "Stories & Poems"
layout: archive
author_profile: true
classes: wide
permalink: /writings/
entries_layout: grid
search: false
pagination:
    enabled: true
    category: writings
---

{% assign alltags = site.categories['writings'] | sort %} 
{% assign grouptag =  alltags | map: 'tags' | join: ','  | split: ','  | group_by: tag | sort: 'name' %}
<ul class="taxonomy__index">
  {% for tag in grouptag %}
    <li>
      <a href="{{ site.baseurl }}{{ tag.name }}">
        <strong>{{ tag.name }}</strong> <span class="taxonomy__count">{{ tag.size }}</span>
      </a>
    </li>  
  {% endfor %}
</ul>
<p class="notice">Prefer to read a series from the beginning? <a href="/haleys-war/">Haley's War</a> is an unfinished chaotic fever dream, but it's a helluva ride.</p>

<div class="entries-{{ page.entries_layout }}">
{% for post in paginator.posts %}
  {% include archive-single.html type=page.entries_layout %}
{% endfor %}
</div>

{% include paginator.html %}
