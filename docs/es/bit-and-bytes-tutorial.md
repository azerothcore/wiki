---
redirect_from: "/Bit-and_bytes-tutorial"
---

# Tutorial de Bits y Bytes 

## Introducción

En informática, los números se representan internamente en binario. Esto significa que, cuando usa un tipo entero para una variable, esto se representará internamente como una suma o concatenación de ceros y unos.

![Byte](http://schoolcoders.com/w/images/0/07/Byte.png)

También puede verlo así:

![Hobbyte](https://ih0.redbubble.net/image.474456834.0620/ap,550x550,12x12,1,transparent,t.u1.png)

¡Esto también es cierto para los booleanos! Si tuviera un bit que fuera igual a 1 o un booleano que fuera igual a verdadero, no habría diferencia en el valor de ambas variables.

Si bien esto es cierto para la salida del valor, un booleano ocupa un byte completo.
Eso es porque no puede simplemente pedir prestado solo 1 bit, por lo que para definir un bool, necesita 1 byte u 8 bits.

Como sabrá, un solo bit representa un 0 o un 1. Una concatenación de ocho de esos bits representa un Byte. El valor máximo de un byte es 255, que es la suma de todos los bits. Cada bit tiene un "valor" y la suma de todos los bits es lo que llamamos máscara. Por ejemplo, el valor del primer bit es 1, el valor del segundo bit es 2 * el valor del bit a su derecha.




``` c++
// Esto es lo mismo que decir que 2^N=x, por ejemplo
2^0=1
2^1=2
2^2=4
2^3=8
2^4=16
2^5=32
2^6=64
2^7=128

/*
 * Puede representar un byte como una secuencia de ceros y unos en consecuencia.
 * Leyendo así, se lee el orden de los bits
 * de derecha a izquierda
 * <-----
*/
1   = 0 0 0 0 0 0 0 1
2   = 0 0 0 0 0 0 1 0
4   = 0 0 0 0 0 1 0 0
8   = 0 0 0 0 1 0 0 0
16  = 0 0 0 1 0 0 0 0
32  = 0 0 1 0 0 0 0 0
64  = 0 1 0 0 0 0 0 0
128 = 1 0 0 0 0 0 0 0
```

Cuando un número tiene 4 bytes de longitud, esto significa que su número realmente usa 32 bits del almacenamiento interno:

00000000 00000000 00000000 00000000

El tipo de datos entero de 32 bits puede contener valores enteros en el rango de −2,147,483,648 a 2,147,483,647. También puede referirse a este tipo de datos como firmado int o unsigned. Unsigned int significa que el tipo de datos de 32 bits unsigned int puede contener valores enteros en el rango de 0 a 4.294.967.295.
La razón por la que el int sin signo siempre almacenará más valores positivos que uno con signo es porque usamos los valores negativos del int con signo como positivos y esto duplica la cantidad de valores positivos que puede almacenar en una variable.


## ¿Para qué sirve?

Ahora imagina que quieres crear un programa que contenga un estado, que se basa en varios valores:

``` c++
// Almacena el estado actual de este programa
bool firstValue = true;
bool secondValue = false;

```

O en su lugar, use una única variable entera y use cada bit de sus 8 bits internos para representar los diferentes verdaderos y falsos.

``` c++
// 00000101
int maskValue = 5;
```

Arriba, el primer bit es verdadero, que representa la primera variable. La segunda es falsa, que representa la segunda variable. La tercera verdad. Y así...

Esta es una forma muy compacta de almacenar datos y tiene muchos usos.

Aquí es donde entra en juego el enmascaramiento de bits. Suena complejo, pero en realidad es muy simple.

El enmascaramiento de bits permite al usuario:
1. Editar bits particulares en un byte(s)
2. Verificar si hay valores de bit particulares presentes o no.
3.  Aplicar una máscara a un valor, donde en nuestro caso el valor es nuestro estado 00000101 y la máscara es nuevamente un número binario, que indica los bits de interés. En este caso nuestra máscara es la número 5.

## Operaciones binarias

### Bitwise AND "&"
Operar con bits es bastante similar a configurar condiciones entre dos variables. Digamos que tenemos, por ejemplo:

``` C++
if (1 && !0)
  printf('Esta condición es verdadera');
```

Cualquier valor que no sea 0 siempre será el mismo que verdadero. Esto significa que:

- 1 es cierto
- !0 es lo mismo que decir no falso, lo que significa que !0 es verdadero
- verdadero y verdadero confirma la condición

De esta manera podemos comparar los valores de 2 bits y si ambos son verdaderos, podemos mantener el valor del bit y obtener un resultado final de la misma manera:

``` C++
255 &= 1

// Esto dará como resultado que 255 se convierta en 1 debido a
// F - Falso y T - Verdadero para comparar los bits de 255 y 1
(255) -> 1 1 1 1 1 1 1 1
(1)   -> 0 0 0 0 0 0 0 1
(1)   -> F F F F F F F T
         0 0 0 0 0 0 0 1
         
// Otro ejemplo:
Valor:     00000101
Máscara:   00000100
---- Y ---------
Resultado: 00000100

// En este caso tenemos el valor 5
int MyState = 5;

//  Y queremos eliminar 1 estado de ese valor
MyState &= 4;

/* Esto convertirá nuestro 00000101 (5)
 * en un 00000100 (4)
 */
```

Los ejemplos anteriores son de hecho malos ejemplos de cómo usar cálculos de bits y pueden haberlo dejado con la duda. ¿Por qué no restar simplemente los valores de los números?

5-1 = 4

es más fácil de entender que comparar bytes o bits y es más natural para el lenguaje humano.

El punto en el uso de & en operaciones de bits suele ir acompañado de otro carácter de operación de bits que es el '~'.

Lo que ~ te permite hacer es invertir la máscara de bits, por ejemplo:

``` C++
255 &= ~1; // Esto hará que 255 se convierta en 254 porque:
(255) -> 1 1 1 1 1 1 1 1
(1)   -> 0 0 0 0 0 0 0 1 // El primer bit es verdadero
(~1)  -> 1 1 1 1 1 1 1 0 // invierte los bits en 1 -> 254
(254) -> 1 1 1 1 1 1 1 0
```

imagina una máscara de bits como esta:
1 0 0 0 0 0 0 0 (128)

si se trataba de una operación entera, entonces  128 - 64 = 64

Sin embargo, si intentó eliminar 64 de 128:

```
1 0 0 0 0 0 0 0 &= ~64

(128) 1 0 0 0 0 0 0 0
(64)  0 1 0 0 0 0 0 0
(~64) 1 0 1 1 1 1 1 1
---------------------
(128) 1 0 0 0 0 0 0 0
```

Entonces 128 no cambiaría porque 64 ya está apagado.

Esta es la razón por la que a menudo en los archivos verá variables que agregan nuevos indicadores y eliminan otros.

--- 

### Bitwise OR "|"

Agregar una nueva bandera a una máscara de bits es más fácil que eliminarlos.

Este concepto se aplica como el OR en una condición:

``` C++

if (true || false)
  printf("Esta condición es verdadera");
else if (true || true)
  printf("Esta condición es verdadera");
else if (false || true)
  printf("Esta condición es verdadera");
else if (false || false)
  printf("Esta condición es falsa");
```

Al igual que con dos condiciones, puede comparar 2 bits y obtener una nueva máscara de bits porque, si uno de los bits es verdadero, este valor de bit se convertirá en verdadero. En otras palabras, si tiene 1 o 0, el nuevo valor de la máscara de bits será 1, por ejemplo:

``` C++
// Aquí inicializamos MyState con 5 también conocido como 00000101 si hablamos en lenguaje de bits
int MyState = 5;

// Luego podemos agregarle una máscara con la siguiente sintaxis
MyState |= 128;

// Nuestro resultado final convertirá 5 en 133 debido a esta lógica:
5   -   0 0 0 0 0 1 0 1
128 -   1 0 0 0 0 0 0 0
------- Result --------
133 -   1 0 0 0 0 1 0 1
```

### Bitwise XOR "^"

Este carácter de operador de bits funciona de una manera diferente a la esperada y puede ser difícil encontrar una forma de usarlo.

Imagina tener las siguientes máscaras de bits:

| Máscara de bits | Values |
| --- | --- |
| ```0 1 0 0 1 1 1 0``` | 78
| ```0 0 1 1 0 1 0 0``` | 52
| ```F T T T T F T F``` | XOR Results |
| ```0 1 1 1 1 0 1 0``` | 122

Podría confundirse con lo que acaba de suceder.

Bueno, solo comparamos el bit de la primera máscara y el bit de la segunda máscara y los comparamos. Si son diferentes, el valor final es verdadero. Así es como se vería programáticamente:

``` C++
// Compara los valores de la máscara 1 y 2
// Si son diferentes, la condición XOR es verdadera
for (int i = 0; i < 8; ++i)
{
  if (bitmask_1[i] != bitmask_2[i])
    printf("Esta condición es verdadera")
}
```

### Bitwise left shit "<<"

Esta operación de bit cambiará todos los valores binarios N veces como se especifica. Veamos más profundo:

Si tenemos el siguiente valor en binario X:

```0 0 0 0 0 0 0 1``` (que es 1) 

y hacemos x << 1, entonces x se convertirá en

```0 0 0 0 0 0 1 0``` 

Entonces, según esta regla, mueve todos los bits a la izquierda en uno y agrega un 0 a la derecha
x << 2 movería todos los bits en 2, por lo que x se convertiría en

```0 0 0 0 0 1 0 0``` 

``` C++
// Desplaza el valor "1", "8-1" veces hacia la izquierda
1<<(8-1)

// (8-1) es lo mismo que 7
1<<(7)

// Lo que mueve 000000001 el 1 en ese valor 7 lugares a la izquierda.
// entonces el resultado es 128 o 
10000000
```
---
## Conclusión

[Hoja de trucos tomada de este enlace](https://www.geeksforgeeks.org/bitwise-operators-in-c-cpp/)

Carácter | Operación | Descripción
-- | -- | --
& | AND | Toma dos números como operandos y hace AND en cada bit de dos números. El resultado de AND es 1 solo si ambos bits son
\| | OR | Toma dos números como operandos y hace OR en cada bit de dos números. El resultado de OR es 1 cualquiera de los dos bits es
^ | XOR | Toma dos números como operandos y hace XOR en cada bit de dos números. El resultado de XOR es 1 si los dos bits son diferentes.
\<\< | desplazamiento a la izquierda | Toma dos números, desplaza a la izquierda los bits del primer operando, el segundo operando decide el número de lugares a desplazar.
\>\> | desplazamiento a la derecha | Toma dos números, desplaza a la derecha los bits del primer operando, el segundo operando decide el número de lugares a desplazar.
~ | NOT | Toma un número e invierte todos los bits

# Créditos

Documentación construida con estos artículos en consideración:

https://www.geeksforgeeks.org/bitwise-operators-in-c-cpp/

https://stackoverflow.com/questions/31575691/what-is-a-bitmask-and-a-mask
