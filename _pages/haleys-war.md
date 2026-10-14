---
layout: default
title: "Haley's War"
permalink: /haleys-war/
---
{% assign haley = site.tags['haley'] | sort: 'date' %}
<div class="wrap">
  <header class="page-head">
    <h1>Haley's War</h1>
    <p>An unfinished chaotic fever dream, in order. <a href="{{ '/writings/' | relative_url }}">All stories and poems</a></p>
  </header>
  <ul class="rows">{% for post in haley %}<li>{% include card.html post=post row=true %}</li>{% endfor %}</ul>
</div>
