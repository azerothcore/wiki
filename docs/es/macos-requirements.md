# Requisitos de macOS

| Guía de instalación | |
| :- | :- |
| Este artículo es parte de la Guía de instalación. Puedes leerlo solo o hacer click en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Inicio: Guía de instalación](classic-installation) | [Paso 2: Instalación del Core >>](macos-core-installation) |

| |
| :- |
| MacOS ≥ 11 |
| OpenSSL ≥ 3.0 |
| Boost ≥ 1.74 |
| MySQL ≥ 8.0.0 |
| CMake ≥ 3.16 |

- Instala XCode desde la App Store, luego abre la terminal y escribe:

```sh
xcode-select --install
```

- Instala el gestor de paquetes [Homebrew](http://brew.sh/)

Usa brew para instalar los paquetes necesarios:

```sh
brew update
```

```sh
brew install openssl@3 readline cmake boost coreutils bash bash-completion coreutils
```

Esto instalará bash 5+; puede que necesites reiniciar tu terminal.
Asegúrate de estar usando bash 5 o superior escribiendo `bash --version`.

Ahora instala mysql:

```sh
brew install mysql
```

Se te pedirán algunas instrucciones para completar la instalación de `mysql`, por ejemplo para establecer correctamente una contraseña. Simplemente sigue las instrucciones y configura correctamente mysql. **Este paso es importante, no lo omitas.**

Para verificar que mysql se ha instalado correctamente, intenta acceder a él usando la línea de comandos (por ejemplo, `mysql -u root -p`) o usando gestores de cliente de BD con interfaz gráfica como Sequel Ace.

Puedes instalar Sequel Ace con:

```sh
brew install --cask sequel-ace
```

## Ayuda

Si sigues teniendo problemas, comprueba:

- [Preguntas frecuentes](faq)
- [Errores comunes](common-errors)
- [Cómo pedir ayuda](how-to-ask-for-help)
- [Únete a nuestro servidor de Discord](https://discord.gg/gkt4y2x), pero no es un canal de soporte 24/7. Un miembro del staff te responderá cuando tenga tiempo.

| Guía de instalación | |
| :- | :- |
| Este artículo es parte de la Guía de instalación. Puedes leerlo solo o hacer click en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Inicio: Guía de instalación](classic-installation) | [Paso 2: Instalación del Core >>](macos-core-installation) |
