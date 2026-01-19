---
layout: archive-taxonomy
title: Stories & Poems
permalink: /writings/
taxonomy: writings
entries_layout: grid
search: false
classes: wide
author_profile: false
autopages:
    display_name: Stories & Poems
pagination:
    enabled: true
    category: writings
---

{% if page.header.overlay_color or page.header.overlay_image or page.header.image %}
  {% include page__hero.html %}
{% elsif page.header.video.id and page.header.video.provider %}
  {% include page__hero_video.html %}
{% endif %}

{% if page.url != "/" and site.breadcrumbs %}
  {% unless paginator %}
    {% include breadcrumbs.html %}
  {% endunless %}
{% endif %}

<div id="main" role="main">
  {% include sidebar.html %}

  <div class="archive">
    {% unless page.header.overlay_color or page.header.overlay_image %}
      <h1 id="page-title" class="page__title">{% if page.title %}{{page.title}}{% endif %}</h1>
    {% endunless %}

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

    <div class="entries-{{ page.entries_layout }}">
    {% for post in paginator.posts %}
      {% include archive-single.html type=page.entries_layout %}
    {% endfor %}
    </div>

    {% include paginator.html %}

  </div>

</div>
