# Requisitos macOS

| Guía de instalación | |
| :- | :- |
| Este articulo es una parte de la guía de instalación. Puedes leerlo o hacer clic en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Inicio: Guía de instalación](classic-installation.md) | [Paso 2: Instalación del núcleo >>](macos-core-installation.md) |

| |
| :- |
| Boost ≥ 1.70 |
| MySQL ≥ 5.7.0 |
| CMake ≥ 3.16 |

- Instala XCode usando la App Store, luego abre la terminal y escribe:

```sh
xcode-select --install
```

- Instalar el gestor de paquetes [Homebrew](http://brew.sh/)

Utilice brew it para instalar los paquetes necesarios:

```sh
brew update
```

```sh
brew install openssl@1.1 readline cmake boost coreutils bash bash-completion coreutils
```

Esto instalará bash 5+, puede que necesites reiniciar tu terminal.
Asegúrese de que está utilizando bash 5 o superior escribiendo `bash --versión`.

Ahora instala mysql:

```sh
brew install mysql
```

Se le pedirán algunas instrucciones para completar la instalación de `mysql`, por ejemplo para configurar correctamente una contraseña. Simplemente siga las instrucciones y configure correctamente mysql. **Este paso es importante, no lo omita.**

Para verificar que mysql se ha instalado correctamente, intente acceder a el utilizando la línea de comandos (por ejemplo, `mysql -u root -p`) o utilizando gestores de clientes de BD con una interfaz de usuario como Sequel Ace.

Puedes instalar Sequel Ace con:

```sh
brew install --cask sequel-ace
```

## Ayuda

Si todavía tiene problemas, compruebe:

* [FAQ - Preguntas frecuentes](faq.md)

* [Errores comunes](common-errors.md)

* [Cómo pedir ayuda](how-to-ask-for-help.md)

* [Únase a nuestro servidor de Discord](https://discord.gg/gkt4y2x), pero no es un canal de soporte 24/7. Un miembro del staff le responderá siempre que tenga tiempo.

| Guía de instalación | |
| :- | :- |
| Este articulo es una parte de la guía de instalación. Puedes leerlo o hacer clic en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Inicio: Guía de instalación](classic-installation.md) | [Paso 2: Instalación del núcleo >>](macos-core-installation.md) |
