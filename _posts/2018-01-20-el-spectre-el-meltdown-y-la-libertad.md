---
layout: post
title: El Spectre, el Meltdown y la Libertad
author: germaaan
image:
  feature: banners/header.jpg
tags: mundo-libre vulnerabilidades
---

Mucho se ha hablado últimamente de las vulnerabilidades Spectre y Meltdown que se han encontrado recientemente en una gran cantidad de microprocesadores modernos (como el [artículo](https://www.fwhibbit.es/spectre-y-meltdown) de nuestro amigo [Hartek](https://twitter.com/guille_hartek) de Follow The White Rabbit). Aunque estas vulnerabilidades han afectado a procesadores de todo tipo, hay una empresa que ha quedado especialmente señalada: **Intel**.

Intel (al igual que la mayoría de fabricantes) no te proporcionan una versión accesible del código del software que se ejecuta en el interior de su hardware y sin el que el mismo no puede funcionar, generalmente para esto se alegan _"motivos de seguridad"_. El problema de esto es que tenemos que confiar ciegamente en que la empresa va a hacer bien su trabajo (lo que se ha de presuponer siempre...🌚) y que su prioridad es el bienestar el usuario (🌚🌚🌚...directamente).

Ahora en serio, son cosas que pasan, sí, es difícil explotarlo, también; pero más allá de los detalles técnicos, que una empresa haga oídos sordos durante meses cuando ya se conocía el problema o que incluso [lancen nuevos productos con el conocimiento de que son _"defectuosos"_](https://www.profesionalreview.com/2018/01/05/intel-lanzo-coffee-lake-sabiendo-vulnerable-spectre-meltdown/), no habla precisamente bien de las políticas de esa empresa.

Y si la intención era cuidar su imagen, desde luego no lo están consiguiendo, porque la estrategia de desarrollar el parche en el oscurantismo para lanzarlo justo a la vez que se hiciera público el problema (_"lanzamos el parche ipso facto, y esto en dos días está olvidado"_), realmente no ha solucionado el problema: [el problema sigue estando](https://www.xataka.com/componentes/intel-admite-que-el-parche-para-spectre-provoca-problemas-en-practicamente-todos-sus-procesadores) y su imagen cada vez está quedando más manchada.

En las causas judiciales que se están iniciando se decidirá si estos problemas pueden conllevar acciones punibles que deban ser castigadas por la ley, pero desde luego lo que no parece es muy moral. Y a esto último es a lo que quería llegar. ¿Es necesario que las compañías tengan tanto control sobre nuestros dispositivos a cambio de _"comodidad"_? O más bien, ¿debemos permitir que las compañías hagan lo que quieran con **NUESTRO** hardware por la excusa de que es por nuestro _"bien"_?

Básicamente de esto es sobre lo que se habla en este [artículo](https://www.fsf.org/blogs/sysadmin/the-management-engine-an-attack-on-computer-users-freedom) de la FSF, que más allá de los problemas técnicos que se han producido, habla sobre cómo realmente el problema es que nos encontramos ante un ataque a la libertad de los usuarios.

Es cierto que el argumento de que algo _"siempre que es libre es seguro"_ puede presentar ambigüedades, pero aunque no todo el software libre es auditado por el simple hecho de ser software libre, si existe la opción de que cualquiera con disponibilidad y/o recursos pueda hacerlo. Sin embargo, precisamente lo que estamos viendo es que de forma análoga, **todo el software cerrado** (lo que a su vez representa la mayoría del software empresarial tradicional) **tampoco es seguro**, siendo esto más grave por el simple hecho de que aquí sí hay una compañía que generalmente te hace aceptar unos términos y condiciones de uso a cambio de una garantía de funcionamiento: "tú firma aquí y yo me 'comprometo' a que esto funcione sin que tengas que preocuparte de nada". Eso es falso. "Tú firma aquí y yo me 'comprometo' a sumergirte en una falsa sensación de seguridad" sería más correcto... y más grave. Si se produce un problema, tú solo puedes esperar; incluso si alguien quiere intentar ayudar, él solo puede esperar; si un tercero descubre cómo explotar el problema, tú... creo que te vas a poner hasta a rezar.

Que los sistemas sean cerrados es un problema, que no existan sistemas abiertos es un problema todavía mayor, pero que las compañías (que ya han demostrado que dada la complejidad técnica de las tecnologías actuales hace muy difícil desarrollar productos que sean 100% efectivos y sin fallos) se empeñen en poner todo tipo de impedimentos para que prosperen alternativas libres, es quizás el mayor de los problemas.

Además, la **hipocresía** es incluso mayor cuando vemos que Intel usa para todo esto sistemas operativos como Minix, un sistema operativo libre que por usar una _licencia libre débil_ como es la BSD, permite usar algo hecho de forma desinteresada (y en este caso, para más inri, con objetivos pedagógicos) para restringir el uso de algo que nos pertenece, nuestro propio ordenador. Precisamente para evitar estas paradojas tecnológicas, desde la FSF recomiendan que siempre usemos para nuestros proyectos _licencias libres fuertes_ como la GNU GPLv3 y posteriores, porque aunque pueda sonar restrictivo y contrario a la idea de tener una _"completa libertad"_, aquí vemos que que el software libre se pueda cerrar puede ser contraproducente a la hora de fomentar el propio software libre.

La esperanza que nos queda es que siempre habrá gente con devoción, que ya sea porque su trabajo se lo permita o porque no le importa _"sacrificar"_ su tiempo por el beneficio de tener una sociedad tecnológica libre, tarde o temprano consigue con un enorme esfuerzo romper estas restricciones para tener la opción de precisamente eso: **tener opciones**.









