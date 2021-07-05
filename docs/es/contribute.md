# Contribuir

Puedes contribuir de varias formas a AzerothCore:

- [comentando un problema abierto](Contribute#how-to-comment-an-issue)

- [abriendo un problema](Contribute#how-to-open-an-issue)

- [prueba de una solicitud de extracci�n](How-to-test-a-PR)

- [prueba de cambios solo de base de datos](How-to-test-DB-only-changes)

- [creando una solicitud de extracci�n](Contribute#how-to-create-a-pull-request)

- [mejorando nuestra wiki](Contribute#improve-the-wiki)
## Informaci�n general

Para contribuir, obviamente necesitas una cuenta de github.

## C�mo comentar un problema

Puede ayudar mucho revisando los [problemas](https://github.com/azerothcore/azerothcore-wotlk/issues) y uni�ndose a sus discusiones.

Una cosa que puede hacer es actualizar su n�cleo y verificar si el problema sigue siendo v�lido en su revisi�n, luego puede escribir un comentario **que incluya el hash de confirmaci�n**.

## C�mo abrir un problema

osas importantes que hacer antes de informar un error:

**1) Actualice su n�cleo a la �ltima revisi�n de AzerothCore y compruebe si el error sigue ah�.**

**2) Busque entre los [problemas](https://github.com/azerothcore/azerothcore-wotlk/issues) para verificar si alguien ya inform� el error, en ese caso solo tiene que comentar el problema para confirmar el error (incluida su revisi�n principal)**

Si **(y solo si)** el error a�n no se ha informado, puede [abrir un problema](https://github.com/azerothcore/azerothcore-wotlk/issues/new) e incluir:

- La **descripci�n del error**, incluidos los **enlaces** �tiles y **ID/GUID/nombres** de cualquier entidad relacionada (NPC, hechizos, objetos de juego, etc.)
- La **revisi�n del n�cleo (hash de confirmaci�n)** del AzerothCore en el que est� ejecutando, **no escriba solo la "�ltima versi�n"** incluso si acaba de actualizar su n�cleo.
- Si se trata de un problema de compilaci�n, ser�a �til conocer tambi�n su **sistema operativo** y **versi�n del compilador**.

## C�mo probar una solicitud de extracci�n

- Lea [C�mo probar un PR](How-to-test-a-PR).

## C�mo crear una solicitud de extracci�n

- Lea [C�mo crear un PR](How-to-create-a-PR).

### Dando cr�dito al autor del c�digo

Si desea enviar un c�digo escrito por otra persona, puede otorgarle cr�ditos al autor cuando se comente:

`git commit --author="AuthorName <authoremail@address.com>" -am "Confirma el mensaje aqu�"`

Actualizaci�n: desafortunadamente, al fusionar un PR aplastando el comentario, GitHub establece autom�ticamente al autor del compromiso resultante como la persona que abri� el PR. Por esta raz�n, mencione al autor original (y comprometa, si corresponde) en la descripci�n del PR.

## Mejora la Wiki

�Quieres mejorar o agregar una p�gina a nuestro wiki? �Bien! Discut�moslo usando [nuestro chat](https://discord.gg/PaqQRkd).
