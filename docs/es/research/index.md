---
template: section.html
title: Investigación
title_image_src: /images/inictel-nano.webp
hide:
  - navigation
  - toc
projects:
  - name: Desarrollo de un dispositivo optoelectrónico de bajo costo y banda ancha sintonizando velocidad de grupo en interface RF – Óptica
    description: "El proyecto tiene la finalidad de diseñar, fabricar y caracterizar un dispositivo electroóptico integrado denominado modulador fotónico de silicio."
    image: https://www.inictel-uni.edu.pe/wp-content/uploads/2020/05/Contrato-015-2018.jpg
    url: /research/rf-optica/
  - name: Modulador Electro Óptico
    description: "Desarrollo de un dispositivo opto-electrónico de bajo costo y banda ancha sintonizando velocidad de grupo en interface RF – Óptica"
    image: /images/research/modulador_optoelectrico.webp
    url: https://www.youtube.com/watch?v=Ygg0D-AJ2b0
  - name: Microfluídica
    description: "Lab-on-a-chip: Modelado numérico, microfabricación y caracterización de módulos microfluídicos"
    image: /images/research/microfluidica.webp
    url: https://www.youtube.com/watch?v=fFmk10MSt8I
  - name: Radares
    description: "Estudio de perfiles en el subsuelo mediante métodos de inversión y modelado electromagnético utilizando un geo radar de VHF aplicado a la zona arqueológica de Caral"
    image: /images/research/radares.webp
    url: https://www.youtube.com/watch?v=YzFtC-ZhI_M
  - name: Guía de Onda Complejas
    description: "Fabricación y validación experimental de interconexiones ópticas verticales compactas para plataformas de guías de onda de III-V y Silicio"
    image: /images/research/guias_de_onda.webp
  - name: Sistema de litografía de escritura directa
    description: " "
    image: /images/research/litografia.webp
  - name: Subsistemas Ópticos
    description: " "
    image: /images/research/sistemas_opticos.webp
  - name: Cristales Fotónicos y Metamateriales THZ/IR
    description: " "
    image: /images/research/cristales_fotonicos.webp
---

# Investigación

::cards:: image-bg cols=2
{% for project in projects %}

- title: {{project.name}}
  content: '{{project.description}}
  {% if project.url %}</p><p><a class="md-button md-button--primary" href="{{project.url}}">Ver más :material-open-in-new:</a>{% endif %}
  '
  image: {% if project.image %}{{project.image}}{% else %}https://dummyimage.com/600x400/eee/aaa{% endif %}
  {% endfor %}

::/cards::
