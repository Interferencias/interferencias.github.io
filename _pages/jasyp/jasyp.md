---
layout: page
title: JASYP '18 - Participación
permalink: /jasyp/
description: "Formulario de participación para las JASYP '18"
image:
  feature: banners/header.png
---

Las **JASyP** son unas jornadas organizadas por Interferencias con la colaboración de Follow the White Rabbit y Hack&Beers, que pretende dar cabida a todos aquellos ponentes que quieran hablar de anonimato, seguridad informática y protección digital. La edición de 2017 se celebró en la Escuela Técnica Superior de Ingeniería Informática y Telecomunicaciones de la Universidad de Granada, y acogió a ponentes y asistentes de toda España durante dos días en la Escuela Técnica para acabar con un tercer día de Hack&Beers.

En 2018 pretendemos lanzar la segunda edición de este evento, y esperamos poder aprender mucho, aprovechar los días incluso más, y sacar partido del buen rollo que Granada siempre brinda en sus bares. Para ello lanzamos este **C4P** para todos aquellos interesados en participar como ponentes en el evento.

**¿Qué pedimos?**

- Ponentes interesados en hablar sobre cualquiera de los temas relacionados: **Anonimato en internet, Seguridad Informática y Protección digital.**
- Las charlas pueden ser de cualquier área. Es cierto que la temática se presta a talleres y charlas técnicas, pero nos encantaría acoger una charla relacionada con la temática de **derecho, filosofía, política, arte** o cualquier otra rama. ¡Lánzate y cuéntanoslo!
- Si la charla está apoyada en Software libre o cualquier contenido que sea libre, muchísimo mejor.

**¿Qué ofrecemos?**

Somos un grupo de voluntarios con mucha energía e interés, pero por desgracia no contamos con la solvencia económica suficiente como para pagar a los ponentes de fuera viaje y estancia. Sin embargo,  podemos ofreceros cerveza y tapas gratis, además de mucho buen humor granadino.

Si te gusta como suena, aquí te dejamos el formulario a rellenar. Aceptamos propuestas de ponentes de todas las edades, géneros, etnia y condición social, **seas quien seas, si te gusta la temática ¡Anímate!**

<div class="bootstrap">
	<div class="text-center">
		<h3>Crear participaciones</h3>
		<hr>

		<div class="form-group">
			<form name="reg_form" role="form" class="form-horizontal" method="post" action="http://localhost/jasyp_app/form">
				<input type="hidden" name="good" value="{{ site.url }}/jasyp/success/" />
				<input type="hidden" name="bad" value="{{ site.url }}/jasyp/error/" />
				<label for="name" style="margin: 0 auto;">Nombre:</label>
				<input type="text" name="name" class="form-control" style="width: 250px; margin: 0 auto;" required minlength="2" maxlength="255" pattern="[a-zA-ZÁáÉéÍíÓóÚúñÑÇç ]+" oninvalid="this.setCustomValidity('Introduce una cadena con entre 2 y 255 caracteres alfabéticos')"
				 oninput="setCustomValidity('')" />
				<label for="email" style="margin: 0 auto;">Email:</label>
				<input type="email" name="email" class="form-control" style="width: 250px; margin: 0 auto;" required maxlength="255" oninvalid="this.setCustomValidity('Introduce una dirección de correo eletrónico válida')" oninput="setCustomValidity('')" />
				<label for="title" style="margin: 0 auto;">Título:</label>
				<input type="text" name="title" class="form-control" style="width: 350px; margin: 0 auto;" required minlength="20" maxlength="255" pattern="[a-zA-Z0-9ÁáÉéÍíÓóÚúñÑÇç.,-: ]+" oninvalid="this.setCustomValidity('Introduce una cadena con entre 20 y 255 caracteres alfanuméricos o signos de puntuación')"
				 oninput="setCustomValidity('')" />
				<label for="type">Tipo:</label>
				<p>
					<input type="radio" name="type" value="T" required oninvalid="this.setCustomValidity('Selecciona una de las dos opciones')" oninput="setCustomValidity('')" /> Charla &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
					<input type="radio" name="type" value="W" /> Taller
				</p>
				<label for="length">Duración:</label>
				<p>
					<input type="radio" name="length" value="S" required oninvalid="this.setCustomValidity('Selecciona una de las dos opciones')" oninput="setCustomValidity('')" /> Corta &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
					<input type="radio" name="length" value="L" /> Larga
				</p>
				<label for="title">Resumen:</label>
				<textarea name="abstract" required class="form-control" style="resize:none; overflow-y: scroll;" rows="4" cols="50" required minlength="150" maxlength="2000" pattern="[a-zA-Z0-9ÁáÉéÍíÓóÚúñÑÇç.,-: ]+ " oninvalid="this.setCustomValidity('Introduce una cadena con entre 150 y 2000 caracteres alfanúmericos o signos de puntuación')"
				 oninput="setCustomValidity('')"></textarea>
				<div class="col-xs-12" style="height:12px;"></div>
				<button type="submit" class="btn btn-default">Enviar</button>
			</form>
		</div>
	</div>
</div>
