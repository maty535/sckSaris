---
layout: page
title: "Registračný formulár zraz 2026"

forms:
  - to: saris@cykloklub.sk
    subject: Registrácia na zraz 2026
    redirect: /
    form_engine: formspree
    placeholders: false
    fields: 
      - name: name
        input_type: text
        placeholder: Meno a Priezvisko
        required: true
      - name: email
        input_type: email
        placeholder: Email adresa
        required: true
      - name: mobil
        input_type: text
        placeholder: Mobil
        required: true
      - name: tricko
        input_type: text
        placeholder: Velkosť trička
        required: true
      - name: klub
        input_type: text
        placeholder: Klubová príslušnosť
        required: false
      - name: poznaka
        input_type: text
        placeholder: Poznámka, alebo špeciálny odkaz pre organizátorov zrazu
        required: true
      - name: submit
        input_type: submit
        placeholder: Submit form
        required: true
---

{% if page.forms[0] %}
{::nomarkdown}
{% include form.html form="0" %}
{:/nomarkdown}
{% endif %}