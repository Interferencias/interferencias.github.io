---
layout: post
title: La encriptación y los números primos
author: nacheteam
image:
  feature: banners/header.jpg
tags: encriptación números-primos mersenne
---

### La encriptación y los números primos  

Todos utilizamos sin darnos cuenta los números primos al entrar a nuestra cuenta del banco, al pagar en bitcoins o cuando nos metemos en cualquier web que use el protocolo HTTPS. ¿En qué se usan para estas aplicaciones?  
La respuesta es sencilla: en la encriptación.  
Para empezar tenemos que repasar qué conocemos por encriptación y cómo funciona.

#### Encriptación  

La encriptación se encarga de, a partir de un mensaje, convertirlo en una maraña de números, letras o cualquier otra cosa que no nos sea fácilmente legible y no nos permita volver al mensaje original de forma fácil ni rápida. Para esto tenemos mil algoritmos que ya se han enfrentado al hecho de convertir mensajes en códigos cifrados y no nos preocupa esta vez.  
El problema interesante para nosotros son las claves que se usan en estos algoritmos. Cuando se encripta un mensaje podemos escoger la clave que queremos que se use para cifrarlo, de esta forma si dos personas distintas encriptan el mismo fichero, al haber usado dos claves diferentes, tendrán ficheros encriptados diferentes. Para cada mensaje que queramos cifrar tenemos esencialmente dos tipos de algoritmos: con clave simétrica o con clave pública-privada.  
La primera opción es la más simple y también la más rápida, ya que usamos la misma clave tanto para encriptar como para desencriptar. En este caso la clave es escogida por el usuario pudiendo ser una cadena de caracteres cualquiera como la que tendríamos de contraseña en cualquier cuenta de correo u otro servicio.  
La segunda opción por contra es mucho más robusta. En esta opción el usuario no puede escoger su clave pública ni privada ya que vienen predeterminadas. Imaginemos que Antonio quiere mandar un mensaje a María. Para esto lo primero que haría Antonio es coger la clave pública de María y encriptar, usando un algoritmo, el mensaje. Tras esto se lo manda a María y a esta solo le resta coger su clave privada y desencriptarlo; fácil. En resumen lo que hacemos es encriptar con la clave pública y desencriptar con la clave privada. Aquí es donde los primos aparecen.  
Las claves públicas son generadas usando dos números primos p y q. Se toman estos dos primos y se multiplican, lo que da la clave pública. La clave privada contiene los dos números primos p y q que son los dos únicos factores de la clave pública, es decir p y q son los únicos primos que cumplen que $p\cdot q$ = clave_pública.  
A esto se le suma que la forma de encriptar y desencriptar es:  
- C = $M^e$ mod(n)
- M = $C^d$ mod(n)  
Donde:  
- M es el mensaje en texto plano expresado como un número entero.  
- C es el mensaje encriptado expresado como un entero.  
- n es el producto de p y q.  
- d es un número entero aleatorio primo relativo con $(p-1)\cdot (q-1)$ (esto es que su máximo común divisor sea 1).  
- e es el inverso multiplicativo de d.

Resumiendo: usamos $p\cdot q$ como clave pública y p y q como clave privada.  
Ahora imaginemos que una tercera persona quiere desencriptar el mensaje dirigido a María sólo conociendo la clave pública. Esto lo que nos deja es que necesitamos factorizar la clave pública para obtener la clave privada, suena fácil, ¿verdad?  
Estos cálculos evidentemente no son tan sencillos. El algoritmo más fácil para buscar un primo (en el caso general) es tomar todos los números que estén por debajo de la raíz cuadrada e ir probando uno a uno si son divisores de nuestro número.  
Por ejemplo si tenemos el número 1459160519 tendríamos que comprobar hasta el número 38199, lo cual sería fácilmente computable por un ordenador. Date cuenta de que hemos tomado un número de 10 dígitos. Ahora vamos a tomar uno de 400 (el primo más grande conocido tiene 22,338,618 dígitos). Si tomamos uno de 400 tenemos que la raíz cuadrada tiene 200 dígitos. El tiempo de vida del universo es $10^{18}$ segundos, por lo que si asumimos que un ordenador comprueba un millón de divisores por segundo tenemos que podemos comprobar $10^{24}$ posibilidades en todo el tiempo de vida del universo. En un número de 400 dígitos son $10^{200}$ posibilidades para probar, por lo que necesitaríamos ejecutar nuestro programa $10^{176}$ veces el tiempo de vida del universo.  
Ahora estamos un terreno cómodo, ya que con primos relativamente grandes (100 dígitos o más), con los métodos actuales no es posible hallar en un tiempo razonable la descomposición en primos.  

Por lo tanto si queremos hacer sistemas de encriptación muy seguros tenemos que tomar primos lo más grandes posibles, Mersenne nos va a ayudar.

#### Primos de Mersenne  

Para hallar números primos muy grandes no podemos ir probando todos los números en orden, ya que no sería computable en un tiempo razonable.  
Mersenne (1588-1648) propuso que los números de la forma $2^p-1$ podían ser primos, sabiéndose en la actualidad además que tienen propiedades muy deseables para eliminar candidatos que no sean primos.  
Como ejemplo podemos poner que $2^{2} - 1 = 3$ es un primo de Mersenne y $2^3 - 1 = 7$ lo es también.  
Esta es la forma actual en la que hallamos primos muy grandes siendo el último hallado en Enero de 2016 con 22.338.618 dígitos y siendo este número $2^{74.207.281} - 1$.  
Estos primos pueden llegar a ser un poco difíciles de manejar, pero son muy útiles y podemos usarlos para sistemas muy robustos de encriptación. Actualmente la asociación [GIMPS](https://www.mersenne.org/) tiene una red distribuida para hallar primos de Mersenne que tiene el récord de haber hallado el último número primo mencionado anteriormente.  
Los números de Mersenne tienen propiedades muy buenas que nos permiten calcular muy rápido estos primos como se puede observar en un [programa de prueba](https://github.com/nacheteam/Mersenne-primes) que he hecho. Si quieres aprender mas puedes echar un ojo al repositorio anterior y mirar la web de GIMPS donde explican de forma muy didáctica cómo los comprueban.

Las matemáticas son una herramienta esencial a la hora de defender nuestra privacidad y anonimato.  

_\#somosruido_  
_\#wearenoise_
