# AzerothCore Wiki

Leer en: [English :en:](README.md) | [Español :es:](README_es.md)

Wiki para el proyecto AzerothCore disponible aquí: https://www.azerothcore.org/wiki/es/home

¡Bienvenido a la Wiki de AzerothCore! Este repositorio ofrece documentación completa para configurar y personalizar el emulador de WoW de AzerothCore.

Si quieres contribuir a la wiki, abre una solicitud de registro (PR) en el directorio /docs/.

¿Tienes algún problema? [Abre una incidencia](https://github.com/azerothcore/wiki/issues/new).

## Creación y gestión de AzerothCore Wiki localmente

Para construir y ejecutar el sitio wiki localmente para probar sus cambios, necesitará [instalar Ruby](https://www.ruby-lang.org/en/documentation/installation/#rubyinstaller) en su sistema.

Una vez hecho esto, instala el paquete:
```sh
gem install bundler
```

Tras instalar el paquete, clona el repositorio y cambia el directorio en tu shell a la raíz del repositorio extraído. Para instalar las gemas necesarias, ejecuta el siguiente comando:
```sh
bundle install --gemfile=./.env-files/Gemfile.github 
```

Ahora que nuestras gemas están instaladas, podemos construir el sitio y ejecutarlo para ver cómo se ven nuestros cambios:
```sh
bundle exec --gemfile=./.env-files/Gemfile.github jekyll serve --destination _site --baseurl /wiki --verbose --open-url
```