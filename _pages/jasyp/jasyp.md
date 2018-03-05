---
layout: page
title: JASYP '18 - Participación
permalink: /jasyp/
description: "Formulario de participación para las JASYP '18"
image:
  feature: banners/header.png
timing: false
---

Las **JASYP** (*Jornadas sobre Anonimato, Seguridad y Privacidad*) son unas jornadas organizadas por [Interferencias](https://twitter.com/Inter_ferencias) con la colaboración de [Follow the White Rabbit](https://twitter.com/fwhibbit_blog) y [Hack&Beers](https://twitter.com/hackandbeers), que pretende dar un espacio a todas aquellas personas con inquietudes sobre los problemas que encontramos en el día a día cada vez que usamos Internet o cualquier ordenador en general. La edición de 2017 se celebró en la [Escuela Técnica Superior de Ingenierías Informática y de Telecomunicación de la Universidad de Granada](https://etsiit.ugr.es/), recibiendo a parcitipantes y asistentes de toda España durante dos días en el Salón de Actos de la propia Escuela, para cerrar con un tercer día en el que se celebró un **Hack&Beers** en el bar **La Posada**.

![cartel_privacidad_etsiit]({{ "/assets/images/jasyp/17/01.jpg" }})

En este 2018 pretendemos lanzar la segunda edición de este evento, donde esperamos poder aprender mucho, aprovechar los días incluso más, y sacar partido del buen rollo que Granada siempre brinda en sus bares. Para ello lanzamos este **Call for Papers** para todas aquellas personas interesadas en participar en la **edición de este año**, que tendrá lugar **los días VIERNES 13 Y SÁBADO 14 DE ABRIL**.

<div class="bootstrap">
	<div class="text-center">
    <br>
		<h3>¿Qué pedimos?</h3>
		<hr>
  </div>
</div>

- Personas interesadas en hablar sobre la importancia de los **derechos digitales**, la **privacidad en Internet**, la **seguridad informática** y todos aquellos temas de este ámbito que puedan tener relación.
- Las charlas pueden ser de cualquier área. Es cierto que la temática se presta a talleres y charlas técnicas, pero nos encantaría acoger una charla relacionada con la temática desde un punto de vista distinto, como puede ser el de personas dedicadas a **derecho, filosofía, política, arte** o cualquier otra rama. ¡Lánzate y cuéntanoslo!
- Si la charla está apoyada en Software Libre o cualquier contenido que sea libre, muchísimo mejor.
- Además, también vamos a organizar un concurso artístico sobre el que podréis encontrar más información [aquí]({{ site.url }}/jasyp/concurso/).
- Y como complemento a todo esto, también estamos preparando un **Capture The Flag**, donde cualquiera que se anime pueda poner a prueba sus habilidades a la hora de explotar las debilidades de sistemas informáticos (las bases de participación serán publicadas próximamente).

![cartel_privacidad_etsiit]({{ "/assets/images/jasyp/17/02.jpg" }})

<div class="bootstrap">
	<div class="text-center">
    <br>
		<h3>¿Qué ofrecemos?</h3>
		<hr>
  </div>
</div>

Los integrantes de Interferencias somos un grupo de personas con mucha energía e interés, pero por desgracia no contamos con la suficiente solvencia económica como para poder hacernos cargo de los gastos de viaje y alojamiento para los participantes que tengan que desplazarse. Sin embargo, podemos ofreceros cerveza y tapas gratis, además de mucho buen humor granadino.

Es por eso que también estamos buscando patrocinadores que nos ayuden a cubrir estos gastos que nos gustaría poder afrontar de cara a hacer un evento de una mayor magnitud. Puedes encontrar más información sobre cómo patrocinar las JASYP en [esta página]({{ site.url }}/jasyp/patrocinio/) o escribiendo al correo [jasyp@interferencias.tech](mailto:[jasyp@interferencias.tech]).

<div class="bootstrap">
	<div class="text-center">
    <br>
		<h3>¿Te hemos convencido?</h3>
		<hr>
  </div>
</div>

En el caso de sea así, si todo esto te suena bien, aquí te dejamos el formulario a rellenar; aunque también agradecemos enormemente que nos ayudes con la difusión del evento a través de redes sociales o el simple boca a boca. Aceptamos propuestas de participantes de todas las edades, géneros, etnias y condición social, **seas quien seas, si te gusta la temática ¡Anímate!**

![cartel_privacidad_etsiit]({{ "/assets/images/jasyp/17/03.jpg" }})

<div class="bootstrap">
	<div class="text-center">
    <br>
		<h3>Registrar participación</h3>
		<hr>

		<div class="form-group">
			<form name="reg_form" role="form" class="form-horizontal" method="post" action="{{ site.url }}/jasyp_app/form">
				<input type="hidden" name="good" value="{{ site.url }}/jasyp/success/" />
				<input type="hidden" name="bad" value="{{ site.url }}/jasyp/error/" />
				<label for="name" style="margin: 0 auto;">Nombre:</label>
				<input type="text" name="name" class="form-control" style="width: 250px; margin: 0 auto;" required minlength="2" maxlength="255" pattern="[a-zA-ZÁáÉéÍíÓóÚúñÑÇç ]+" oninvalid="this.setCustomValidity('Introduce una cadena con entre 2 y 255 caracteres alfabéticos')"
				 oninput="setCustomValidity('')" />
				<label for="email" style="margin: 0 auto;">Email:</label>
				<input type="email" name="email" class="form-control" style="width: 250px; margin: 0 auto;" required maxlength="255" oninvalid="this.setCustomValidity('Introduce una dirección de correo eletrónico válida')" oninput="setCustomValidity('')" />
				<label for="title" style="margin: 0 auto;">Título:</label>
				<input type="text" name="title" class="form-control" style="width: 350px; margin: 0 auto;" required minlength="20" maxlength="255" pattern="[a-zA-Z0-9ÁáÉéÍíÓóÚúñÑÇç.,-:¿?¡! ]+" oninvalid="this.setCustomValidity('Introduce una cadena con entre 20 y 255 caracteres alfanuméricos o signos de puntuación/exclamación')"
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
				<textarea name="abstract" required class="form-control" style="resize:none; overflow-y: scroll;" rows="4" cols="50" required minlength="150" maxlength="2000" oninvalid="this.setCustomValidity('Introduce una cadena con entre 150 y 2000 caracteres alfanúmericos o signos de puntuación')"
				 oninput="setCustomValidity('')"></textarea>
				<div class="col-xs-12" style="height:12px;"></div>
				<button type="submit" class="btn btn-default">Enviar</button>
			</form>
		</div>
	</div>
</div>
