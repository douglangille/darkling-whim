---
layout: archive
title: "Recently Revised"
permalink: /revised/
entries_layout: grid
classes: wide
author_profile: true
search: false
---

{% assign posts = site.tags['revised'] %}
<div class="entries-{{ page.entries_layout }}">
{% for post in posts %}
    {% include archive-single.html type=page.entries_layout %}
{% endfor %}
</div>
