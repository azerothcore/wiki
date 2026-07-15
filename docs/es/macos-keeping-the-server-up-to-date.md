# macOS: mantener el servidor actualizado

| Guía de instalación | |
| :- | :- |
| Este artículo es parte de la Guía de instalación. Puedes leerlo solo o hacer click en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Paso 6: Pasos finales del servidor](es/final-server-steps) | [Paso 8: Configuración del cliente >>](es/client-setup) |

## Mantener el código fuente actualizado

```sh
cd ~/azerothcore/
git pull origin master
```

```sh
cd build
make -j 8; make install
```

A veces añadimos o eliminamos archivos del repositorio. En ese momento es necesario recompilar el servidor, tal como se instaló la primera vez [en la Instalación del Core en macOS](es/macos-core-installation#configuring-for-compiling).

## Mantener la base de datos actualizada

Lee [Base de datos: mantener el servidor actualizado](es/database-keeping-the-server-up-to-date)

## Ayuda

Si sigues teniendo problemas, comprueba:

- [Preguntas frecuentes](es/faq)
- [Errores comunes](es/common-errors)
- [Cómo pedir ayuda](es/how-to-ask-for-help)
- [Únete a nuestro servidor de Discord](https://discord.gg/gkt4y2x), pero no es un canal de soporte 24/7. Un miembro del staff te responderá cuando tenga tiempo.

| Guía de instalación | |
| :- | :- |
| Este artículo es parte de la Guía de instalación. Puedes leerlo solo o hacer click en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Paso 6: Pasos finales del servidor](es/final-server-steps) | [Paso 8: Configuración del cliente >>](es/client-setup) |
