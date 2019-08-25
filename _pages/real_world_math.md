---
layout: archive
title: "Real World Math"
permalink: /real_world_math/
author_profile: true
---

{% include base_path %}

This is a collection of projects that I've worked on that show how interesting mathematical concepts affect things we do everyday.


{% for post in site.working_papers reversed %}
  {% include archive-single.html %}
{% endfor %}
