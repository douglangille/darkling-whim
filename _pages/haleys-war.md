---
layout: archive
title: "Haley's War"
permalink: /haleys-war/
entries_layout: grid
classes: wide
author_profile: true
---

{% assign posts = site.tags['haley'] | sort: 'date'  %}
<div class="entries-{{ page.entries_layout }}">
{% for post in posts %}
    {% include archive-single.html type=page.entries_layout %}
{% endfor %}
</div>