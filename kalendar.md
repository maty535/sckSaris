---
layout: page
title: Kalendár
description: Infomácie o cykloakciách v roku 2026
categories: akcie
tags: akcie kalendar 2026
permalink: /calendar/
akcie:
  - { d: "2026-01-18", t: "18.1.2026", n: "Hermanovský Šlid Bežky", z: "(Hrečko)" }
  - { d: "2026-04-26", t: "26.4.2026", n: "Otvorenie cyklosezóny", z: "(Sabol)", 
      gpx: "2026-04-26-OtvorenieSezony-MatosSabol" , url: "https://earth.google.com/earth/d/1o51LmGenyDSoFCYgID8GZHvzeACqDyrs?usp=sharing" }
  - { d: "2026-05-10", t: "10.5.2026", n: "Prejazd trasy zrazu na 1. deň zrazu", z: "(Hrečko)",
    gpx: "2026-05-10-Zraz-Trasa1",
    url: "https://mapy.com/sk/turisticka?planovani-trasy&dim=6a022ce4f4aafc2fc8505da5&x=21.4013645&y=48.9082719&z=12" }
  - { d: "2026-05-24", t: "24.5.2026", n: "Prejazd trasy zrazu na 2. deň zrazu", z: "(Hrečko)" , 
      gpx: "2026-05-24-Zraz-Trasa-den2",
      url: "https://mapy.com/sk/turisticka?planovani-trasy&dim=6a26a1093a0d25a773300457&x=21.2675431&y=49.0031098&z=12" }
  - { d: "2026-06-07", t: "7.6.2026", n: "Prejazd trasy zrazu na 3. deň zrazu", z: "(Hrečko)",
       gpx: "2026-06-07-Zraz-trasa-den3", 
       url: "https://mapy.com/sk/turisticka?planovani-trasy&dim=6a26a940bcbcce8bb4c822c1&x=21.2354102&y=48.9978578&z=14" }
  - { d: "2026-06-19", t: "19.-21.6.2026", n: "NZC SCK Sigord Savore", z: "(SCK Šariš Prešov)" }
  - { d: "2026-07-01", t: "x. 7.2026", n: "Slovenský kras", z: "(Fil)" , 
      gpx: "SNV-JanoFil", 
      url: "https://mapy.com/sk/turisticka?planovani-trasy&dim=69eba8bab62416099118d361&x=20.5762808&y=48.9397628&z=12" }
  - { d: "2026-07-26", t: "26.7.2026", n: "Levočské vrchy", z: "(Holinga)" }
  - { d: "2026-08-01", t: "1.8.2026", n: "Slovenský raj", z: "(predseda)" }
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

<style>
  .highlight-next {
    background-color: #fff3cd !important;
    font-weight: bold;
  }
  table { width: 100%; border-collapse: collapse; }
  th, td { text-align: left; padding: 8px; border-bottom: 1px solid #ddd; }
  
  /* Voliteľné: jemné vizuálne odlíšenie starých akcií */
  .stara-akcia {
    opacity: 0.6;
  }
</style>

<table id="tabulka-akcii">
  <thead>
    <tr>
      <th>Dátum</th>
      <th>Názov akcie</th>
      <th>Zodpovedný</th>
      <th>Gpx</th>
      <th>Prieskum</th>
    </tr>
  </thead>
  <tbody>
    {% for akcia in page.akcie %}
      <tr data-datum="{{ akcia.d }}">
        <td>{{ akcia.t }}</td>
        <td>{{ akcia.n }}</td>
        <td>{{ akcia.z }}</td>
        <td>
          {% if akcia.gpx %}
            {% capture gpx_url %}/assets/trasy/{{ akcia.gpx }}.gpx{% endcapture %}
            <a href="{{ gpx_url | relative_url }}">GPX</a>
          {% endif %}
        </td>
        <td>
          {% if akcia.url %}
            <a href="{{ akcia.url }}">Prieskum</a>
          {% endif %}
        </td>
      </tr>
    {% endfor %}
  </tbody>
</table>

<script>
  document.addEventListener("DOMContentLoaded", function() {
    // Získanie dnešného dátumu vo formáte YYYY-MM-DD (v lokálnom čase)
    const dnes = new Date();
    const dnesString = dnes.getFullYear() + '-' + 
                       String(dnes.getMonth() + 1).padStart(2, '0') + '-' + 
                       String(dnes.getDate()).padStart(2, '0');

    // Výber všetkých riadkov tabuľky, ktoré majú dátum
    const riadky = document.querySelectorAll("#tabulka-akcii tbody tr");
    let najdene = false;

    riadky.forEach(function(riadok) {
      const datumAkcie = riadok.getAttribute("data-datum");
      
      if (datumAkcie) {
        if (datumAkcie >= dnesString && !najdene) {
          riadok.classList.add("highlight-next");
          najdene = true; // Zvýrazníme iba prvú nasledujúcu akciu
        } else if (datumAkcie < dnesString) {
          // Voliteľné: pridanie triedy pre staré akcie (napr. zosivenie textu)
          riadok.classList.add("stara-akcia");
        }
      }
    });
  });
</script>