# Red

| Guía de Instalación | |
| :- | :- |
| Este artículo es parte de la Guía de Instalación. Puede leerlo solo o hacer click en los links previos para navegar con facilidad entre los pasos. |
| [<< Paso 4: Instalación de la Base de Datos](database-installation.md) | [Paso 6: Pasos finales >>](final-server-steps.md) |

Esta guía está pensada para configuraciones avanzadas o para, simplemente, proveer más detalles en la configuración de su servidor para uso local o en linea. En general, la configuración por defecto explicada en la guía particular para cada sistema operativo debería funcionar para instalaciones simples.

## Configuraciones de Worldserver y Authserver

Para casi todos los escenarios básicos de instalación, las configuraciones por defecto de IP: localhost (127.0.0.1) deberían dejarse tal cual. La bindip (0.0.0.0) predeterminada debería dejarse tal cual también.

### Configurando el realmlist de la base de datos auth para conexiones por internet 

Acá es donde se debe usar la IP de internet, de manera que los clientes puedan encontrar su servidor a través de internet. Debe tener los puertos 3724 (authserver) y 8085 (worldserver) disponibles, o abrirlos desde su router / firewall.

**Realmlist Table**

Asegurese de que su aplicación **authserver** direcciona las conexiones entrantes hacia su reino.

- Ejecute su herramienta de administración de bases de datos elegida (ejemplo. SQLYog or HeidiSQL)

- Si necesita conectarse a su base de datos desde una máquina externa, lea: https://www.enovision.net/mysql-ssh-tunnel-heidisql en lugar de abrir los puertos para MySQL server.

- Abra la base de datos **acore_auth** y busque la tabla **realmlist**. Necesitará editar el **address field** de acuerdo con sus necesidades:

    - LAN IP (192.168.x.x) - Si está instalando AzerothCore en un computador diferente al computador en el que ejecuta WoW, pero todos los computadores involucrados están en la misma red (router) use la IP de red de area local de ese computador.

    - 127.0.0.1 - También conocida como "localhost". Deje esta configuración tal cual si instaló AzerothCore en el mismo computador en el que corre WoW y solo usted conectará a él.

    - IP Externa– Si usted quiere que otras personas se conecten a su servidor, use una IP externa. Visite http://www.whatismyip.com/ para encontrar su dirección de IP externa.

<br>

## Ayuda

Si sigue teniendo inconvenientes, revise:

* [Preguntas frecuentes](faq.md)

* [Errores Comunes](common-errors.md)

* [Cómo solicitar ayuda](how-to-ask-for-help.md)

* [Unase a nuestro discord](https://discord.gg/gkt4y2x). Aunque no es un canal de soporte 24/7, un miembro del staff le responderá siempre que tenga tiempo.


| Guía de Instalación | |
| :- | :- |
| Este artículo es parte de la Guía de Instalación. Puede leerlo solo o hacer click en los links previos para navegar con facilidad entre los pasos. |
| [<< Paso 4: Instalación de la Base de Datos](database-installation.md) | [Paso 6: Pasos finales del Servidor >>](final-server-steps.md) |