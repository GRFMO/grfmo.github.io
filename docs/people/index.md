---
template: section.html
title_image_src: /images/home.jpeg
hide:
  - path
  - navigation
coordinators:
  - name: Roxana María Morán Morales
    degree: Licenciada en Ingeniería Electrónica
    email: rmoran@inictel-uni.edu.pe
    image: /images/people/roxana_moran.jpeg
    url: https://ctivitae.concytec.gob.pe/appDirectorioCTI/VerDatosInvestigador.do?id_investigador=272
principals:
  - name: Ruth Esther Rubio Noriega
    degree: Doctora en Ingeniería Eléctrica en el Área de Telecomunicaciones y Telemática
    email: rrubio@inictel-uni.edu.pe
    image: https://dina.concytec.gob.pe/appDirectorioCTI/UploadFotoPath.do?tipo=visualizar_archivo&id_investigador=117349&ruta=/documents/docInvestigadores/117349/imagenes/ruthy_square.jpg&content_type=image/jpeg
    url: https://dina.concytec.gob.pe/appDirectorioCTI/VerDatosInvestigador.do?id_investigador=117349
  - name: María Elisia Armas Alvarado
    degree: Doctora en Ingeniería Eléctrica
    email: marmas@inictel-uni.edu.pe
    image: https://dina.concytec.gob.pe/appDirectorioCTI/UploadFotoPath.do?tipo=visualizar_archivo&id_investigador=47104&ruta=/documents/docInvestigadores/47104/imagenes/Mary%20renacyt.jpg&content_type=image/jpeg
    url: https://dina.concytec.gob.pe/appDirectorioCTI/VerDatosInvestigador.do;jsessionid=35152b29a8cef863cc8671d28ab2?id_investigador=47104
  - name: Luz Antuanet Adanaqué Infante
    degree: MsC. en Ingeniería Electrónica (2014)
    email: ladanaque@inictel-uni.edu.pe
    image: /images/people/antuanet_adanaque.jpg
    url: https://dina.concytec.gob.pe/appDirectorioCTI/VerDatosInvestigador.do;jsessionid=eb87b9547ff5dec2bcdb04f9b4fe?id_investigador=24693
associate:
  - name: Jorge González Reaño
    degree: Doctor en Ciencias de la Computación
    email: jgonzalez@utec.edu.pe
    image: /images/people/jorge_gonzalez.jpeg
    url: https://ctivitae.concytec.gob.pe/appDirectorioCTI/VerDatosInvestigador.do?id_investigador=0177054
postgraduate:
  - name: Marco Antonio Becerra Pérez
    degree: Bachiller en Ingeniería Mecatrónica (2022)
    studies: Estudiante de Maestría en Ingeniería Matemática por la Universidad Nacional de Trujillo
    email: mbecerra@inictel-uni.edu.pe
    image: /images/people/marco_becerra.jpg
  - name: Freddy Orlando Jara Poma
    degree: Bachiller en Ingeniería de Telecomunicaciones (2018)
    studies: Estudiante de Maestría en Ingeniería Eléctrica en el área de Telecomunicaciones y Telemática - UNICAMP
    email: f236485@dac.unicamp.br
    image: /images/people/freddy_jara.png
  - name: Wilfredo Pedro Acevedo Elguera
    degree: Licenciado en Telecomunicaciones (2010)
    studies: Estudiante de Maestría en Telecomunicaciones por la Universidad Nacional de Ingeniería
    email: wilfredo.acevedo.e@uni.pe
    image: /images/people/pedro_acevedo.jpg
graduate:
  - name: Licely Tatiana Javier Astete
    degree: Bachiller en Ingeniería Electrónica (2021)
    email: licely.javier@unmsm.edu.pe
    image: /images/people/tatiana_javier.jpg
  - name: Gabriel Andrés Arias Obregón
    degree: Egresado de Ingeniería Electrónica (2022)
    email: gariaso@uni.pe
    image: /images/people/gabriel_arias.jpg
  - name: Ten Sun Ly Salinas Lazarte
    degree: Bachiller en Ingeniería Mecatrónica (2023)
    email: u201425313@upc.edu.pe
    image: /images/people/ten_salinas.jpg
  - name: Roosevelt Jhans Ubaldo Chavez
    degree: Bachiller en Ciencia de la Computación (2022)
    email: roosevelt.ubaldo@utec.edu.pe
    image: /images/people/roosevelt_ubaldo.png
initiation:
  - name: Franck David Soria Pinedo
    degree: Estudiante de pregrado en Ingeniería Electrónica (2023)
    email: fsoria@inictel-uni.edu.pe
    image: /images/people/franck_soria.jpg
  - name: Villon Mariluz Roger Daniel
    degree: Estudiante de pregrado en Ingenieria Electrónica( 2023)
    email: rvillonm@uni.pe
    image: /images/people/roger_villon.jpg
---

# Miembros

## Coordinadora

::cards:: image-bg
{% for user in coordinators %}

- title: {{user.name}}
  content: '{{user.degree}}</p><p>
  <a href="mailto:{{user.email}}" class="mailto">:fontawesome-solid-envelope: {{user.email}}</a>
  '
  image: {% if user.image %}{{user.image}}{% else %}https://dummyimage.com/600x400/eee/aaa{% endif %}
  {% if user.url %}url: {{user.url}}{% endif %}
  {% endfor %}

::/cards::

## Investigadoras Principales

::cards:: image-bg
{% for user in principals %}

- title: {{user.name}}
  content: '{{user.degree}}</p><p>
  <a href="mailto:{{user.email}}" class="mailto">:fontawesome-solid-envelope: {{user.email}}</a>
  '
  image: {% if user.image %}{{user.image}}{% else %}https://dummyimage.com/600x400/eee/aaa{% endif %}
  {% if user.url %}url: {{user.url}}{% endif %}
  {% endfor %}

::/cards::

## Investigadores Asociados

::cards:: image-bg
{% for user in associate %}

- title: {{user.name}}
  content: '{{user.degree}}</p><p>
  <a href="mailto:{{user.email}}" class="mailto">:fontawesome-solid-envelope: {{user.email}}</a>
  '
  image: {% if user.image %}{{user.image}}{% else %}https://dummyimage.com/600x400/eee/aaa{% endif %}
  {% if user.url %}url: {{user.url}}{% endif %}
  {% endfor %}
  ::/cards::

## Estudiantes de Posgrado

::cards:: image-bg
{% for user in postgraduate %}

- title: {{user.name}}
  content: '{{user.degree}}</p><p class="nt-card-text">{{user.studies}}</p><p>
  <a href="mailto:{{user.email}}" class="mailto">:fontawesome-solid-envelope: {{user.email}}</a>
  '
  image: {% if user.image %}{{user.image}}{% else %}https://dummyimage.com/600x400/eee/aaa{% endif %}
  {% if user.url %}url: {{user.url}}{% endif %}
  {% endfor %}
  ::/cards::

## Graduados

::cards:: image-bg
{% for user in graduate %}

- title: {{user.name}}
  content: '{{user.degree}}</p><p>
  <a href="mailto:{{user.email}}" class="mailto">:fontawesome-solid-envelope: {{user.email}}</a>
  '
  image: {% if user.image %}{{user.image}}{% else %}https://dummyimage.com/600x400/eee/aaa{% endif %}
  {% if user.url %}url: {{user.url}}{% endif %}
  {% endfor %}
  ::/cards::

## Iniciación Científica

::cards:: image-bg
{% for user in initiation %}

- title: {{user.name}}
  content: '{{user.degree}}</p><p>
  <a href="mailto:{{user.email}}" class="mailto">:fontawesome-solid-envelope: {{user.email}}</a>
  '
  image: {% if user.image %}{{user.image}}{% else %}https://dummyimage.com/600x400/eee/aaa{% endif %}
  {% if user.url %}url: {{user.url}}{% endif %}
  {% endfor %}
  ::/cards::
