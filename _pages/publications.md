---
layout: archive
title: "Publications/Presentations"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

This section contains a variety of projects that I've presented in formal settings.

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
