---
hide:
  - path
  - navigation
principals:
  - name: Ruth Esther Rubio Noriega
    degree: Doctora en Ingeniería Eléctrica en el Área de Telecomunicaciones y Telemática 
    email: rrubio@inictel-uni.edu.pe
    image: ../images/people/ruth_rubio.jpg
    url: /people/ruth-rubio
  - name: María Elisia Armas Alvarado 
    degree: Doctora en Ingeniería Eléctrica
    email: marmas@inictel-uni.edu.pe
    image: ../images/people/maria_armas.jpg
    url: /people/maria-armas
  - name: Luz Antuanet Adanaqué Infante
    degree: MsC. en Ingeniería Electrónica (2014)
    email: ladanaque@inictel-uni.edu.pe
    image: ../images/people/antuanet_adanaque.jpg
    url: /people/luz-adanaque
associate:
  - name: Jorge González Reaño
    degree: Doctor en Ciencias de la Computación
    email: jgonzalez@utec.edu.pe
    image: https://utec.edu.pe/sites/default/files/pictures/picture-941-1602617091.png
postgraduate:
  - name: Marco Antonio Becerra Pérez
    degree: Estudiante de Maestría en Matemáticas
    email: mbecerra@inictel-uni.edu.pe
    image: ../images/people/marco_becerra.jpg
  - name: Freddy Orlando Jara Poma
    degree: Bachiller en Ingeniería de Telecomunicaciones (2018)
    email: f236485@dac.unicamp.br
    image: https://dummyimage.com/600x400/eee/aaa
  - name: Wilfredo Pedro Acevedo Elguera 
    degree: Lic. Telecomunicaciones (2010)
    email: wilfredo.acevedo.e@uni.pe
    image: https://dummyimage.com/600x400/eee/aaa
graduate:
  - name: Licely Tatiana Javier Astete
    degree: Bachiller en Ingeniería Electrónica (2021)
    email: licely.javier@unmsm.edu.pe
    image: ../images/people/tatiana_javier.jpg
  - name: Gabriel Andrés Arias Obregón
    degree: Egresado de Ingeniería Electrónica (2022)
    email: gariaso@uni.pe
    image: ../images/people/gabriel_arias.jpg
  - name: Ten Sun Ly Salinas Lazarte
    degree: Bachiller en Ingeniería Mecatrónica (2023)
    email: u201425313@upc.edu.pe
    image: ../images/people/ten_salinas.jpg
  - name: Roosevelt Jhans Ubaldo Chavez
    degree: Bachiller en Ciencia de la Computación (2022)
    email: roosevelt.ubaldo@utec.edu.pe
    image: ../images/people/roosevelt_ubaldo.jpeg
initiation:
  - name: Franck David Soria Pinedo
    degree: Estudiante de pregrado en Ingeniería Electrónica (2023)
    email: fsoria@inictel-uni.edu.pe
    image: ../images/people/franck_soria.jpg
  - name: Villon Mariluz Roger Daniel
    degree: Estudiante de pregrado en Ingenieria Electrónica( 2023)
    email: rvillonm@uni.pe
    image: ../images/people/roger_villon.jpg

---

# Miembros

## Investigadoras Principales



::cards:: image-bg
{% for user in principals %}
- title: {{user.name}}
  content: '{{user.degree}}</p><p>
            <a ref="mailto:{{user.email}}" class="mailto">:fontawesome-solid-envelope: {{user.email}}</a>
          '
  image: {{user.image}}
  url: {{user.url}}
{% endfor %}

::/cards::

## Investigadores Asociados

::cards:: image-bg
{% for user in associate %}
- title: {{user.name}}
  content: '{{user.degree}}</p><p>
            <a ref="mailto:{{user.email}}" class="mailto">:fontawesome-solid-envelope: {{user.email}}</a>
          '
  image: {{user.image}}
{% endfor %}
::/cards::

## Estudiantes de Posgrado

::cards:: image-bg
{% for user in postgraduate %}
- title: {{user.name}}
  content: '{{user.degree}}</p><p>
            <a ref="mailto:{{user.email}}" class="mailto">:fontawesome-solid-envelope: {{user.email}}</a>
          '
  image: {{user.image}}
{% endfor %}
::/cards::

## Graduados

::cards::  image-bg
{% for user in graduate %}
- title: {{user.name}}
  content: '{{user.degree}}</p><p>
            <a ref="mailto:{{user.email}}" class="mailto">:fontawesome-solid-envelope: {{user.email}}</a>
          '
  image: {{user.image}}
{% endfor %}
::/cards::

## Iniciación Científica

::cards:: image-bg
{% for user in initiation %}
- title: {{user.name}}
  content: '{{user.degree}}</p><p>
            <a ref="mailto:{{user.email}}" class="mailto">:fontawesome-solid-envelope: {{user.email}}</a>
          '
  image: {{user.image}}
{% endfor %}
::/cards::

