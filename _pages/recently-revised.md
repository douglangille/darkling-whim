---
layout: default
title: "Recently Revised"
permalink: /recently-revised/
---
{% assign revised = site.tags['revised'] | sort: 'revised' | reverse %}
<div class="wrap">
  <header class="page-head">
    <h1>Recently Revised</h1>
    <p>Old stories that got a little love and polish. <a href="{{ '/writings/' | relative_url }}">All stories and poems</a></p>
  </header>
  <ul class="rows">{% for post in revised %}<li>{% include card.html post=post row=true %}</li>{% endfor %}</ul>
</div>
