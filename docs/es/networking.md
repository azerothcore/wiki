# Red

| Guía de instalación | |
| :- | :- |
| Este artículo es parte de la Guía de instalación. Puedes leerlo solo o hacer click en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Paso 4: Instalación de la base de datos](es/database-installation) | [Paso 6: Pasos finales del servidor >>](es/final-server-steps) |

Esta guía está pensada para configuraciones avanzadas o simplemente para dar más detalles sobre cómo configurar tu reino para uso local o por internet. En general, la configuración por defecto explicada en la guía específica de tu sistema operativo debería ser suficiente para instalaciones simples.

## Configuraciones de Worldserver y Authserver

Para casi todos los escenarios de configuración básica, la configuración de IP por defecto localhost (127.0.0.1) debería dejarse tal cual. La bindip por defecto (0.0.0.0) también debería dejarse tal cual.

### Configurar el realmlist de la base de datos auth para conexiones por internet

Aquí es donde tienes que usar tu IP de internet para que los clientes de internet puedan encontrar tu servidor. Necesitas tener los puertos 3724 (authserver) y 8085 (worldserver) redirigidos o abiertos en tu router/firewall, usando el protocolo TCP.

**Realmlist Table**

Necesitas asegurarte de que tu aplicación **authserver** dirija las conexiones entrantes hacia tu reino.

- Ejecuta tu herramienta de gestión de base de datos elegida (p. ej. SQLYog o HeidiSQL) o la interfaz de línea de comandos (CLI) de MySQL.

- Si necesitas conectarte a tu base de datos desde una máquina externa, lee https://www.enovision.net/mysql-ssh-tunnel-heidisql en lugar de abrir los puertos del servidor MySQL.

- Abre la base de datos **acore_auth** y busca la tabla **realmlist**. Necesitas editar el **campo address** según tus necesidades:

    - IP LAN (192.168.x.x) - Si estás instalando AzerothCore en un equipo distinto a aquel en el que ejecutas WoW, pero todos los equipos involucrados están en la misma red (router), usa la IP de red de área local de ese equipo.

    - 127.0.0.1 - También conocida como "localhost". Deja esta configuración tal cual, aquí y en tus configs, si instalaste AzerothCore en el mismo equipo en el que ejecutas WoW y solo tú te conectas a él.

    - Dirección IP pública – Si quieres que otras personas se conecten a tu servidor, usa tu IP externa. Visita http://www.whatismyip.com/ para encontrar tu dirección IP externa.
        - Si lo alojas desde una red doméstica, probablemente necesitarás configurar las redirecciones de puertos adecuadas, lo cual queda fuera del alcance de esta guía. https://portforward.com tiene guías para la mayoría de los routers, y tu proveedor de internet debería poder ayudarte con esto.

    - Nombre de dominio completo (mydomain.com o warcraft.mydomain.com) - Similar a una dirección IP externa, se usaría si quieres que otras personas se conecten a tu servidor con la ventaja añadida de no tener que seguir una IP potencialmente dinámica.
        - Igual que con la dirección IP pública, es probable que necesites configurar redirecciones de puertos si lo alojas desde una red doméstica.
        - Además, necesitarás configurar el DNS para que apunte a la IP pública del servidor. Configurar el DNS queda fuera del alcance de esta guía, aunque tu registrador de dominios o proveedor de DNS dinámico debería tener esta documentación disponible.

{% include note.html content="Si usas HeidiSQL, asegúrate de estar en la pestaña Data cuando edites los valores." %}

 - Comandos de la CLI de MySQL (este paso no es necesario si usaste un gestor de MySQL como HeidiSQL)
    - `$ sudo mysql`
    - Deberías ver que el prompt cambia a mysql>
    - `use acore_auth`;
    - **Reemplaza tu IP con la que hayas elegido usar de arriba**
    - `UPDATE realmlist SET address = '[tu_ip]' WHERE id = 1;`
    - exit

## Ayuda

Si sigues teniendo problemas, comprueba:

- [Preguntas frecuentes](es/faq)
- [Errores comunes](es/common-errors)
- [Cómo pedir ayuda](es/how-to-ask-for-help)
- [Únete a nuestro servidor de Discord](https://discord.gg/gkt4y2x), pero no es un canal de soporte 24/7. Un miembro del staff te responderá cuando tenga tiempo.

| Guía de instalación | |
| :- | :- |
| Este artículo es parte de la Guía de instalación. Puedes leerlo solo o hacer click en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Paso 4: Instalación de la base de datos](es/database-installation) | [Paso 6: Pasos finales del servidor >>](es/final-server-steps) |
