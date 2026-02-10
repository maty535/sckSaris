---
layout: page
title: História
description: Niečo z histórie
permalink: /historia/
---

Vyhľadávanie: <!-- Search Input --> <input type="text" id="search-input" placeholder="Vyhľadávať v histórii...">

<!-- Results Display -->
<ul id="search-results"></ul>

<!-- Initialization Script -->
<script>
  SimpleJekyllSearch({
	limit: 25, // Nastavte na ľubovoľné číslo alebo 1000 pre "všetky"
    searchInput: document.getElementById('search-input'),
    resultsContainer: document.getElementById('search-results'),
    json: '/search.json',
    searchResultTemplate: '<li>{datum} <a href="{url}" title="{title}">{title}</a></li>',
    noResultsText: 'Nenašiel sa žiadny príspevok'
  });
</script>

{%- for post in site.posts -%}
  {%- capture current_year -%}{{ post.date | date: "%Y" }}{%- endcapture -%}
  {%- unless current_year == previous_year -%}
    <h2>{{ current_year }}</h2>
	
    {%- assign previous_year = current_year -%}
  {%- endunless -%}
     <article class="post-item">
	 	- {{post.date | date: "%d. %m. %Y" }}  <a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a>
	  </article>
{%- endfor -%}


## 2025 

- Členská schôdza schválila návrh termínu a miesta konania **25NZC**, termín konania zrazu bude **19.-21.6.2026**, centrom zrazu bude zariadenie **Savore na Sigorde**

<img width="1600" height="962" alt="image" src="https://github.com/user-attachments/assets/22b88e28-6f97-4f8d-8d49-1cb027cafa50" />

