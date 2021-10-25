# Hospedaje de AzerothCore a través de Amazon AWS

Prefacio: El objetivo de esta guía es que se realice principalmente a través de una línea de comandos. También existe la [Consola de AWS] (https://aws.amazon.com/console/) que algunos encontrarán más intuitiva, sin embargo, para la longevidad de la guía (ya que la interfaz de usuario de la Consola de AWS puede cambiar), la herramienta aws-cli será recomendado. También se incluirán comandos grep para recibir solo la salida requerida. Si desea obtener la salida completa, simplemente elimine el `| grep` y todo lo que le sigue.

------

[TOC]

------

## Requisitos previos

Estas herramientas son necesarias ya que el resto del tutorial se realizará a través de una línea de comando habilitada para bash:

- [Cuenta de Amazon AWS](https://portal.aws.amazon.com/billing/signup#/start)
- [Git](https://git-scm.com/downloads)
- [Python](https://www.python.org/downloads/) - asegúrese de verificar que esto se agregue a PATH si usa Windows

------

## AWS-CLI

### Instalación de AWS-CLI

En primer lugar, verifique que Python y su herramienta pip incluida estén configurados correctamente:

```bash
python --version && pip --version
```

Esto debería devolver tanto la versión de python como la de pip. Si no es así, instale Python correctamente y vincúlelo a la RUTA. Ahora que Python está instalado, instale aws-cli a través de:

```bash
pip install awscli --upgrade
```

Verifique que awscli se haya instalado correctamente ingresando `aws --version`. Si no se instaló correctamente, consulte [esto] (https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html#install-post) para solucionar el problema según el funcionamiento del sistema operativo de su computadora.

### Configuración de AWS-CLI

Se requerirá una clave de acceso y una identificación. Esto se puede encontrar en [Credenciales de seguridad de AWS] (https://console.aws.amazon.com/iam/home#/security_credentials) y seleccionando el botón Claves de acceso> Crear nueva clave de acceso. ** Mantenga esta clave segura, ya que puede usarse para realizar cualquier acción en una cuenta de AWS **. Se considera una buena práctica permitir el acceso a través de un [Usuario de IAM] (https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html), especialmente si los privilegios de AWS se compartirán con otra persona. Una vez que se haya obtenido la clave, úsela para otorgar credenciales a aws-cli usando el comando:

```bash
aws configure
```

Inserte el ID y la clave en sus campos correspondientes. Para el nombre de región predeterminado, inserte `us-east-1` y para el formato de salida predeterminado inserte` table`. Ahora se puede encontrar otro servidor con el comando:

```bash
aws ec2 describe-regions --output table
```

Utilice el comando `ping` más los distintos puntos finales para probar la latencia en las regiones. Después de encontrar un servidor apropiado, ejecute `aws configure` nuevamente e ingrese a la nueva región.

### Creación de un par de claves

Antes de que se creen instancias de servidor, se requerirá un [par de claves](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html). Este par de claves se utilizará para validar el acceso a las instancias EC2 a las que está adherido. Cree un nuevo par de claves a través de:

```bash
aws ec2 create-key-pair --key-name AzCore-KP --query 'KeyMaterial' --output text > ~/AzCore-KP.pem
```

El par de claves se guardará en el directorio $HOME. Asegúrese de mantener seguro este archivo `AzCore-KP.pem` recién creado, ya que ** este archivo no se puede rehacer ** después de su creación. Si el par de claves se pierde después de vincularlo a cualquier instancia EC2, será necesario rehacerlo con un nuevo par de claves. El par de claves se utiliza para SSH en la instancia y no hay forma de eliminar el acceso del par de claves sin eliminar finalmente la instancia EC2. Antes de que se pueda utilizar el par de claves, los permisos deben establecerse con:

```bash
chmod 400 ~/AzCore-KP.pem
```

### Creación de una VPC

*Nota: Aunque AWS proporciona una VPC predeterminada que funcionará bien. La información necesaria para crear una VPC completamente nueva para esta guía se proporcionará en caso de que la VPC predeterminada para cualquier caso no esté disponible o no funcione. Al mismo tiempo, actúa como una exploración más profunda de AWS y sus funciones de red.*

Creando una VPC para la región usando:

```bash
aws ec2 create-vpc --cidr-block 172.32.0.0/16 | grep -Po "(vpc)-[a-zA-Z0-9]*\s"
```

Esto debería generar el vpc-id. Guárdelo ya que será necesario más adelante.

También se necesita el comando:

```bash
aws ec2  modify-vpc-attribute --enable-dns-hostnames --vpc-id $VPC_ID 
```

### Creación de una subred

Es necesario vincular una subred con la VPC mediante:

```bash
aws ec2 create-subnet --cidr-block 172.32.0.0/20 --vpc-id $VPC_ID | grep -Po "(?<!\/)(subnet)-[a-zA-Z0-9]*\s"
```

Guarde el valor del ID de subred para usarlo más adelante.

### Creación de una puerta de enlace a Internet

Cree y conecte la puerta de enlace de Internet con:

```bash
aws ec2 create-internet-gateway | grep -Po "(igw)-[a-zA-Z0-9]*\s"
aws ec2 attach-internet-gateway --internet-gateway-id $IGW_ID --vpc-id $VPC_ID
```

### Creación de una tabla de ruta

La VPC recién creada viene con una tabla de rutas incluida, sin embargo, no tiene acceso a una puerta de enlace de Internet de forma predeterminada. Para solucionar este problema, describa las tablas de enrutamiento con:

```bash
aws ec2 describe-route-tables
```

Esto devolverá una tabla con todas las VPC de la región. Busque el que tenga el bloque CIDR utilizado, que probablemente sea `172.32.0.0/16` y guarde el valor de` RouteTableID`. Después de encontrar la identificación de la tabla de ruta, ingrese:

```bash
aws ec2 create-route --route-table-id $RouteTableID --destination-cidr-block 0.0.0.0/0 --gateway-id $IGW_ID
```

### Creación de un Grupo de Seguridad

El grupo de seguridad proporcionará acceso a los puertos necesarios para el tráfico al servidor. Esto se hace mediante:

```bash
aws ec2 create-security-group --group-name AzerothCore --description "World / Auth / SSH Port Access" --vpc-id $VPC_ID | grep -Po "(sg)-[a-zA-Z0-9]*\s"
```

### Configuración del Grupo de Seguridad

La siguiente cadena crea los permisos de tráfico de puertos que permiten el tráfico en los puertos 22 (SSH), 8085 (World Server) y 3724 (Authentication Server). Donde $SECURITY_GROUP_ID es la salida obtenida previamente.

```bash
aws ec2 authorize-security-group-ingress --group-id $SECURITY_GROUP_ID --ip-permissions IpProtocol=tcp,FromPort=22,ToPort=22,IpRanges='[{CidrIp=0.0.0.0/0, Description="SSH from Anywhere"}]' IpProtocol=tcp,FromPort=8085,ToPort=8085,IpRanges='[{CidrIp=0.0.0.0/0, Description="World-Server from Anywhere"}]' IpProtocol=tcp,FromPort=3724,ToPort=3724,IpRanges='[{CidrIp=0.0.0.0/0, Description="Auth-Server from Anywhere"}]'
```

### Encontrar una AMI

 [Ubuntu 18.04 LTS](https://console.aws.amazon.com/ec2/home?region=us-east-1#launchAmi=ami-024a64a6685d05041) se utilizará para la guía, pero cualquier distribución de Linux debería estar bien. Tenga en cuenta que puede haber pequeñas idiosincrasias con distribuciones diferentes. Se pueden encontrar versiones de AMI más recientes de Ubuntu [aquí](https://cloud-images.ubuntu.com/locator/ec2/) y otras AMI que se encuentran en  [AWS Marketplace](https://aws.amazon.com/marketplace/ref=csl_ec2_ami). La AMI que se utiliza para la guía es `ami-024a64a6685d05041`. Encuentre más información sobre esta imagen con:

```bash
aws ec2 describe-images --image-ids ami-024a64a6685d05041
```

### Ejecutando la Instancia

Ahora es el momento de crear la instancia del servidor. Inserte la AMI descrita anteriormente o una nueva en lugar de $AMI_ID :

```bash
aws ec2 run-instances --image-id $AMI_ID --instance-type t2.micro --count 1 --associate-public-ip-address --key-name AzCore-KP --security-group-ids $SECURITY_GROUP_ID --subnet-id $SUBNET_ID
```

Esto creará e inicializará una instancia t2.micro. *Solo se puede ejecutar constantemente una instancia en un mes sin pagar por horas de servidor adicionales.*

### Modificar el Volumen

Ahora, describe la instancia en ejecución con:

```bash
aws ec2 describe-instances
```

Busque la instancia en ejecución y ejecute el siguiente comando en el ID de volumen adjunto:

```bash
aws ec2 modify-volume --size 20 --volume-id $VOL_ID
```

*Esto cambiará el almacenamiento a 20GB. 30GB es el almacenamiento en bloque MAX para el nivel gratuito. ¡Trate de no pasar por alto eso a menos que tenga la intención de pagar!*

### Asignación de una IP Estática

Ejecute el comando:

```bash
aws ec2 allocate-address --domain $VPC_ID
```

Esto proporcionará un ID de asignación. Ahora, usando el ID de instancia que se puede encontrar en el `aws ec2 describe-instances` ejecutado anteriormente, ejecute el comando:

```bash
aws ec2 associate-address --allocation-id $ALLOC_ID --instance-id $INSTANCE_ID
```

*Si se desea un dominio para la conexión, considere el servicio [Amazons Route 53] (https://aws.amazon.com/route53/). Se pueden encontrar a tan solo 12$ por año.*

------

## La Instancia

### SSH en la instancia

Describe la instancia con `aws ec2 describe-instances` y busca el `PublicDnsName`.

Accede al servidor usando el comando:

```bash
SSH -i "~/AzCore-KP.pem" ubuntu@$PublicDnsName
```

### Instalación de AzerothCore

Siga la parte de Linux de la guía que se encuentra en <http://www.azerothcore.org/wiki/Installation>. Ejecute `sudo apt-get update && sudo apt-get upgrade` antes de instalar las dependencias y actualizar los parches de seguridad.

### Subiendo archivo de datos al servidor

Descargue [newest_data.zip](https://mega.nz/#F!Am4DBKCR!o9Qj_xFLfsg4sczqg0xq2A) y descomprímalo y sus subcarpetas. Luego `cd` en la carpeta donde se encuentra y ejecute el comando:

```bash
tar zcfv ~/data.tar.gz newest_data/
```

Esto comprimirá el archivo en un archivo tar.gz. Ahora para subirlo al servidor usando

```bash
scp -i "~/AzCore-KP.pem" ~/data.tar.gz ubuntu@$PublicDnsName:$CMAKE_INSTALL_PREFIX/data
```

Esto puede llevar un tiempo dependiendo de la velocidad de carga. $CMAKE_INSTALL_PREFIX será la ruta hacia donde está instalado el servidor, no el repositorio git clonado que es `~/azeroth-server/` por defecto.

Ahora descomprímelo con:

```bas
tar xfv $CMAKE_INSTALL_PREFIX/data.tar.gz --strip-components=2
```

Ahora debería descomprimirse en `$CMAKE_INSTALL_PREFIX/data/`

Alternativamente, tomado de [stackoverflow](https://stackoverflow.com/a/49444877) y con un rendimiento de descarga mucho mejor:

```bash
#!/bin/bash
fileid="12XIh3rqm3ukpSKQtMop44U4XCYb6kdda"
filename="data.tar.gz"
curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=${fileid}" > /dev/null
curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=${fileid}" -o ${filename}
```

Ejecute `nano $CMAKEINSTALL_PREFIX/data/` y guarde este script como un archivo .`sh` en el directorio de datos y ejecute `chmod -x $filename.sh` para hacerlo ejecutable. El script descargará un [newest_data](https://mega.nz/#F!Am4DBKCR!o9Qj_xFLfsg4sczqg0xq2A) desde Google Drive [upload](https://drive.google.com/open?id=12XIh3rqm3ukpSKQtMop44U4XCYb6kdda). *nota: recomiendo verificar que los valores de la suma de comprobación SHA256 coincidan entre la carga mega y la carga de la unidad de Google. De lo contrario, los archivos no se manipulan ni se modifican.*


### Configuración de la base de datos

Ingrese a MySQL usando `sudo mysql`. Se necesitará un nombre de usuario y contraseña para acceder a la base de datos.

```sql
GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost' IDENTIFIED BY 'password';
```

Los archivos .conf deberán editarse con el nombre de usuario y la contraseña recién elegidos que se describen [aquí](http://www.azerothcore.org/wiki/Installation#4-setting-the-configuration-files).

### Problema de Kswapd  

*Nota: si se ejecuta en una instancia más potente, este paso probablemente sea irrelevante. Para la instancia t2.micro con 1 GB de RAM, se requiere este paso.*

Como ejercicio de aprendizaje después de la compilación, ejecute un `top -oh% MEM` e intente iniciar el servidor mundial. Eventualmente, se cortará y el servidor dejará de responder. Observe que el proceso que ocupa la mayor parte de la memoria es `kswapd`. El proceso `kswapd` se usa siempre que el uso de la memoria del sistema alcanza un umbral y luego descarga la memoria en un almacenamiento. Sin embargo, la imagen de intercambio predeterminada no asigna suficientes recursos para ejecutar el servidor mundial, por lo que se necesita uno nuevo. [Aquí se pueden encontrar varias soluciones a este problema.] (Https://askubuntu.com/questions/178712/how-to-increase-swap-space) La guía utilizará el [método] `dd` (https: //askubuntu.com/a/178726):

```Bash
#Crea una imagen de intercambio de 3GB y configura un área de intercambio
sudo dd if=/dev/zero of=/media/fasthdd/swapfile.img bs=1024 count=3M
sudo mkswap /media/fasthdd/swapfile.img

#Abre el editor con permisos sudo en /etc/fstab
sudo nano /etc/fstab

# Agregue esta línea a /etc/fstab
/media/fasthdd/swapfile.img swap swap sw 0 0

#Activar la imagen de intercambio
swapon /media/fasthdd/swapfile.img
```

### Conectando al servidor

Busque las instancias Dirección IP pública que se puede encontrar con `aws ec2 describe-instances`. Ingrese el `PublicIpAddress` en su tabla de realmlist` acore_auth`. Puede encontrar más información de conexión [aquí] (http://www.azerothcore.org/wiki/Installation#8-connecting-to-the-server).

------

## Descargo de responsabilidad

​	Muchas de las mejores prácticas no se han seguido en lugar de la brevedad de la guía y la ignorancia general sobre la seguridad de Internet. Algunas cosas que se deben saber y que deben hacerse si planea permitir que cualquier persona acceda a su servidor incluyen:

- [Agregar un usuario de IAM para cualquier persona que necesite acceso a AWS.] (Https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) *No permita que alguien ejecute 100 instancias para extraer bitcoins ... tenga en cuenta que la información de pago se almacena para crear una cuenta y que AWS cobra por hora de servidor utilizada.* **Sea seguro.**
- La capa gratuita de AWS permite ** 750 ** horas de instancia, lo que significa 750/24 = 31,25 días. *Solo se puede ejecutar una instancia ininterrumpida durante un mes sin pagar y el nivel gratuito solo dura 12 meses después de la creación de la cuenta. No reciba cargos no intencionales. ¡Has sido advertido!*
- Por lo general, no permita SSH o privilegios de administrador a otro usuario hasta que haya investigado un poco sobre cómo proteger Linux y no permita a nadie privilegios de root. Solo permita a los usuarios los privilegios mínimos requeridos. Tu seguridad está en tus manos, ¡buena suerte!
