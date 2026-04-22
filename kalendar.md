---
layout: page
title: Kalendár
description: Infomácie o cykloakciách v roku 2026
categories: akcie
tags: akcie kalendar
akcie:
  - { d: "2026-01-18", t: "18.1.2026", n: "Hermanovský Šlid Bežky", z: "(Hrečko)" }
  - { d: "2026-04-26", t: "26.4.2026", n: "Otvorenie cyklosezóny", z: "(Sabol)" }
  - { d: "2026-05-10", t: "10. 5.2026", n: "Prejazd trasy zrazu na 1. deň zrazu", z: "(Hrečko)" }
  - { d: "2026-05-17", t: "17.5.2026", n: "Prejazd trasy zrazu na 2. deň zrazu", z: "(Hrečko)" }
  - { d: "2026-06-07", t: "7.6.2026", n: "Prejazd trasy zrazu na 3. deň zrazu", z: "(Pribula)" }
  - { d: "2026-06-19", t: "19.-21.6.2026", n: "NZC SCK Sigord Savore", z: "(Pastirčák)" }
  - { d: "2026-07-01", t: "?. 7.2026", n: "Slovenský kras", z: "(Fil)" }
  - { d: "2026-07-26", t: "26.7.2026", n: "Levočské vrchy", z: "(Holinga)" }
  - { d: "2026-08-01", t: "?.8.2026", n: "Slovenský raj", z: "(predseda)" }
  - { d: "2026-09-13", t: "13.9.2026", n: "Zlatník", z: "(predseda)" }
  - { d: "2026-12-26", t: "26.12.2026", n: "Štefibowling", z: "(predseda)" }
  - { d: "2026-12-31", t: "31.12.2026", n: "Výstup na Šimonku, rozlúčka s rokom 2026", z: "(predseda)" }
---

# Plán akcií na rok 2026
**SLOVENSKÝ CYKLOKLUB ŠARIŠ – PREŠOV**

* **Web:** [saris.cykloklub.sk](http://saris.cykloklub.sk)
* **E-mail:** saris@cykloklub.sk
* **Tel:** 0903 772 184, Ľubo Hrečko
* **IČO:** 37785699
* **Adresa:** Čergovská 22, 08001 Prešov, Slovenská republika

---

{% assign dnes = "now" | date: "%Y-%m-%d" %}
{% assign najdene = false %}

<style>
  .highlight-next {
    background-color: #fff3cd !important;
    font-weight: bold;
  }
  table { width: 100%; border-collapse: collapse; }
  th, td { text-align: left; padding: 8px; border-bottom: 1px solid #ddd; }
</style>

<table>
  <thead>
    <tr>
      <th>Dátum</th>
      <th>Názov akcie</th>
      <th>Zodpovedný</th>
    </tr>
  </thead>
  <tbody>
    {% for akcia in page.akcie %}
      {% assign css_class = "" %}
      {% if akcia.d >= dnes and najdene == false %}
        {% assign css_class = "highlight-next" %}
        {% assign najdene = true %}
      {% endif %}
      <tr class="{{ css_class }}">
        <td>{{ akcia.t }}</td>
        <td>{{ akcia.n }}</td>
        <td>{{ akcia.z }}</td>
      </tr>
    {% endfor %}
  </tbody>
</table>