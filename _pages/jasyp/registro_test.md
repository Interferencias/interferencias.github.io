---
layout: page
title: CFP Test
permalink: /form_test/
description: "Test CFP"
image:
  feature: banners/header.png
timing: false
---

<script>
function check_pdf() {
  var paper = document.getElementById("paper");

  if (paper.files[0].size > 20971520) {
    alert("El archivo seleccionado es demasiado grande (máximo 20 MB).");
    paper.value = "";
  } else if (paper.files[0].type !== "application/pdf"){
    alert("Debe seleccionar un archivo en formato PDF.");
    paper.value = "";
  };
}
</script>

<div class="bootstrap">
	<div class="text-center">
    <br>
		<h3>Registrar participación</h3>
		<hr>

		<div class="form-group">
			<form name="reg_form" role="form" class="form-horizontal" method="post" enctype="multipart/form-data" action="https://interferencias.tech/medinbio/form">
				<input type="hidden" name="good" value="https://medinbio.es/cfp/" />
				<input type="hidden" name="bad" value="https://medinbio.es/inscripcion-2018/" />
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
					<input type="radio" name="type" value="T" required oninvalid="this.setCustomValidity('Selecciona una de las dos opciones')" oninput="setCustomValidity('')" /> Charla
          <span style="display:inline-block; margin-left: 40px;"></span>
					<input type="radio" name="type" value="P" /> Póster
				</p>
        <label for="paper" style="margin: 0 auto;">Paper:</label><br><br>
        <input type="file" name="paper" id="paper" style="width: 250px; margin: 0 auto;" required  oninvalid="this.setCustomValidity('Selecciona un archivo PDF con un tamaño máximo de 20 MB')" oninput="setCustomValidity('')" onchange="check_pdf()"/>
				<div class="col-xs-12" style="height:12px;"></div>
				<button type="submit" class="btn btn-default">Enviar</button>
			</form>
		</div>
	</div>
</div>
