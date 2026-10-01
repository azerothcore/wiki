# 通过 Amazon AWS 托管 AzerothCore

{% include note.html content="本指南由社区编写，可能不是最新的，也未得到官方支持。" %}

前言：本指南的目标是尽可能通过命令行来完成。有些人可能会觉得 [AWS 控制台](https://aws.amazon.com/console/) 更直观，但为了保证指南的长期有效性（因为 AWS 控制台的界面可能会变化），这里推荐使用 aws-cli 工具。此外还会包含 grep 命令，用于只获取所需的输出。如果想要完整输出，只需去掉 `| grep` 及其后的所有内容。

------

[TOC]

------

## 先决条件

本教程的其余部分将通过支持 bash 的命令行完成，因此需要以下工具：

- [Amazon AWS 账号](https://portal.aws.amazon.com/billing/signup#/start)
- [Git](https://git-scm.com/downloads)
- [Python](https://www.python.org/downloads/) - 如果使用 Windows，请确保已将其添加到 PATH

------

## AWS-CLI

### 安装 AWS-CLI

首先确认 Python 及其自带的 pip 工具已正确安装：

```bash
python --version && pip --version
```

这应会返回 python 和 pip 的版本。如果没有，请正确安装 python 并将其链接到 PATH。python 安装完成后，通过以下命令安装 aws-cli：

```bash
pip install awscli --upgrade
```

输入 `aws --version` 验证 awscli 是否安装正确。如果安装不正确，请根据你的操作系统参考[此文档](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html#install-post)进行故障排查。

### 配置 AWS-CLI

需要一个访问密钥（Access Key）和 ID。可以在 [AWS 安全凭据](https://console.aws.amazon.com/iam/home#/security_credentials) 页面找到，选择“Access Keys > Create New Access Key”按钮即可。**请妥善保管该密钥，因为它可以用于在 AWS 账号上执行任何操作**。最佳实践是通过 [IAM 用户](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html) 授予访问权限，尤其是当 AWS 权限需要与他人共享时。拿到密钥后，使用以下命令将凭据提供给 aws-cli：

```bash
aws configure
```

将 ID 和密钥填入相应的字段。默认区域名称填入 `us-east-1`，默认输出格式填入 `table`。现在可以使用以下命令查找其他服务器：

```bash
aws ec2 describe-regions --output table
```

使用 `ping` 命令配合各个端点来测试各区域的延迟。找到合适的服务器后，再次运行 `aws configure` 并输入新的区域。

### 创建密钥对（Key-Pair）

在创建任何服务器实例之前，需要一个[密钥对](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html)。该密钥对用于验证对它所绑定的 EC2 实例的访问。通过以下命令创建新的密钥对：

```bash
aws ec2 create-key-pair --key-name AzCore-KP --query 'KeyMaterial' --output text > ~/AzCore-KP.pem
```

密钥对将保存到 $HOME 目录。请务必妥善保管新创建的 `AzCore-KP.pem` 文件，因为**该文件一旦创建便无法重新生成**。如果密钥对在绑定到任何 EC2 实例后丢失，则需要使用新的密钥对重新创建这些实例。密钥对用于通过 SSH 登录实例，除非彻底删除 EC2 实例，否则无法从密钥对中移除访问权限！使用密钥对之前，必须使用以下命令设置权限：

```bash
chmod 400 ~/AzCore-KP.pem
```

### 创建 VPC

*注意：虽然 AWS 提供的默认 VPC 也能正常使用，但本指南仍会提供创建全新 VPC 所需的信息，以防默认 VPC 因某种原因不可用或无法工作。同时这也能让你更深入地了解 AWS 及其网络功能。*

使用以下命令为该区域创建 VPC：

```bash
aws ec2 create-vpc --cidr-block 172.32.0.0/16 | grep -Po "(vpc)-[a-zA-Z0-9]*\s"
```

这会输出 vpc-id。请保存它，稍后会用到。

还需要执行以下命令：

```bash
aws ec2  modify-vpc-attribute --enable-dns-hostnames --vpc-id $VPC_ID 
```

### 创建子网（Subnet）

需要使用以下命令将子网与 VPC 关联：

```bash
aws ec2 create-subnet --cidr-block 172.32.0.0/20 --vpc-id $VPC_ID | grep -Po "(?<!\/)(subnet)-[a-zA-Z0-9]*\s"
```

保存 subnet-id 值以供后续使用。

### 创建互联网网关（Internet Gateway）

使用以下命令创建并附加互联网网关：

```bash
aws ec2 create-internet-gateway | grep -Po "(igw)-[a-zA-Z0-9]*\s"
aws ec2 attach-internet-gateway --internet-gateway-id $IGW_ID --vpc-id $VPC_ID
```

### 创建路由表（Route Table）

新建的 VPC 自带一个路由表，但默认情况下它无法访问互联网网关！要解决这个问题，请使用以下命令查看路由表：

```bash
aws ec2 describe-route-tables
```

这会返回该区域内所有 VPC 的表。找到使用该 CIDR 网段（很可能是 `172.32.0.0/16`）的那个 VPC，并保存 `RouteTableID` 值。找到路由表 id 后输入：

```bash
aws ec2 create-route --route-table-id $RouteTableID --destination-cidr-block 0.0.0.0/0 --gateway-id $IGW_ID
```

### 创建安全组（Security Group）

安全组将开放服务器通信所需的端口访问权限。通过以下命令创建：

```bash
aws ec2 create-security-group --group-name AzerothCore --description "World / Auth / SSH Port Access" --vpc-id $VPC_ID | grep -Po "(sg)-[a-zA-Z0-9]*\s"
```

### 配置安全组

下面的命令创建端口流量权限，允许 22（SSH）、8085（世界服务器）和 3724（认证服务器）端口的流量。其中 $SECURITY_GROUP_ID 是之前获取的输出。

```bash
aws ec2 authorize-security-group-ingress --group-id $SECURITY_GROUP_ID --ip-permissions IpProtocol=tcp,FromPort=22,ToPort=22,IpRanges='[{CidrIp=0.0.0.0/0, Description="SSH from Anywhere"}]' IpProtocol=tcp,FromPort=8085,ToPort=8085,IpRanges='[{CidrIp=0.0.0.0/0, Description="World-Server from Anywhere"}]' IpProtocol=tcp,FromPort=3724,ToPort=3724,IpRanges='[{CidrIp=0.0.0.0/0, Description="Auth-Server from Anywhere"}]'
```

### 查找 AMI

本指南将使用最新的 Ubuntu LTS，但任何受 AzerothCore 支持的 Linux 发行版都可以。请注意，不同的发行版可能会存在一些细微的差异。可以在[此处](https://cloud-images.ubuntu.com/locator/ec2/)找到更新的 Ubuntu AMI 版本，其他 AMI 可以在 [AWS Marketplace](https://aws.amazon.com/marketplace/ref=csl_ec2_ami) 上找到。本指南使用的 AMI 是 `ami-024a64a6685d05041`。使用以下命令查看该镜像的更多信息：

```bash
aws ec2 describe-images --image-ids ami-024a64a6685d05041
```

### 运行实例

现在终于可以创建服务器实例了。将前面描述的 AMI 或新的 AMI 填入 $AMI_ID 的位置：

```bash
aws ec2 run-instances --image-id $AMI_ID --instance-type t2.micro --count 1 --associate-public-ip-address --key-name AzCore-KP --security-group-ids $SECURITY_GROUP_ID --subnet-id $SUBNET_ID
```

这将创建并初始化一个 t2.micro 实例。*一个月内只能持续运行一个实例而无需支付额外的服务器小时费用。*

### 修改卷（Volume）

现在使用以下命令查看正在运行的实例：

```bash
aws ec2 describe-instances
```

找到正在运行的实例，对其附加的 volume-id 执行以下命令：

```bash
aws ec2 modify-volume --size 20 --volume-id $VOL_ID
```

*这会将存储改为 20GB。30GB 是免费套餐的最大块存储容量。除非你打算付费，否则尽量不要超过这个限制！*

### 分配静态 IP

运行以下命令：

```bash
aws ec2 allocate-address --domain $VPC_ID
```

这将提供一个分配 ID（Allocation ID）。现在使用之前运行 `aws ec2 describe-instances` 时获得的实例 ID 执行以下命令：

```bash
aws ec2 associate-address --allocation-id $ALLOC_ID --instance-id $INSTANCE_ID
```

*如果需要为连接配置域名，可以考虑 [Amazon Route 53](https://aws.amazon.com/route53/) 服务，其价格最低可至每年 12 美元。*

------

## 实例

### 通过 SSH 登录实例

使用 `aws ec2 describe-instances` 查看实例，并找到 `PublicDnsName `。

使用以下命令访问服务器：

```bash
SSH -i "~/AzCore-KP.pem" ubuntu@$PublicDnsName
```

### 安装 AzerothCore

按照 <http://www.azerothcore.org/wiki/Installation> 指南中的 Linux 部分进行操作。在安装依赖项之前，先运行 `sudo apt-get update && sudo apt-get upgrade` 并更新安全补丁。

### 将数据文件上传到服务器

下载 [newest_data.zip](https://mega.nz/#F!Am4DBKCR!o9Qj_xFLfsg4sczqg0xq2A) 并解压它及其子文件夹。接下来 `cd` 到其所在文件夹并执行以下命令：

```bash
tar zcfv ~/data.tar.gz newest_data/
```

这会将文件打包成 tar.gz 文件。现在使用以下命令将其上传到服务器：

```bash
scp -i "~/AzCore-KP.pem" ~/data.tar.gz ubuntu@$PublicDnsName:$CMAKE_INSTALL_PREFIX/data
```

上传可能需要一些时间，具体取决于上传速度。$CMAKE_INSTALL_PREFIX 是服务器安装的路径，而不是克隆的 git 仓库路径，后者默认为 `~/azeroth-server/`。

现在使用以下命令解压：

```bas
tar xfv $CMAKE_INSTALL_PREFIX/data.tar.gz --strip-components=2
```

现在它应该已被解压到 `$CMAKE_INSTALL_PREFIX/data/` 中。

{% include warning.html content="本节中的 Google Drive 和 MEGA 下载链接已过时，不再可用。" %}

或者，借用自 [stackoverflow](https://stackoverflow.com/a/49444877)，下载性能要好得多：

```bash
#!/bin/bash
fileid="12XIh3rqm3ukpSKQtMop44U4XCYb6kdda"
filename="data.tar.gz"
curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=${fileid}" > /dev/null
curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=${fileid}" -o ${filename}
```

运行 `nano $CMAKEINSTALL_PREFIX/data/` 并将此脚本保存为 data 目录下的 .`sh` 文件，然后执行 `chmod -x $filename.sh` 使其可执行。该脚本将从 Google Drive 的[上传](https://drive.google.com/open?id=12XIh3rqm3ukpSKQtMop44U4XCYb6kdda) 下载重新打包的 [newest_data](https://mega.nz/#F!Am4DBKCR!o9Qj_xFLfsg4sczqg0xq2A)。*注意：我建议验证 MEGA 上传与 Google Drive 上传之间的 SHA256 校验值是否匹配。如果匹配，则说明文件未被篡改或更改。*

### 数据库设置

使用 `sudo mysql` 进入 MySQL。访问数据库需要用户名和密码。

```sql
GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost' IDENTIFIED BY 'password';
```

需要按照[此处](http://www.azerothcore.org/wiki/Installation#4-setting-the-configuration-files)的描述，用新选择的用户名和密码编辑 .conf 文件。

### Kswapd 问题

*注意：如果运行在配置更高的实例上，此步骤可能无关紧要。对于只有 1GB 内存的 t2.micro 实例，此步骤是必需的。*

作为学习练习，编译完成后运行 ` top -oh %MEM` 并尝试启动世界服务器。它最终会卡住，服务器将无响应。注意占用大部分内存的进程是 `kswapd`。当系统内存使用量达到阈值时，就会使用 `kswapd` 进程将内存卸载到存储中。然而，默认的交换镜像没有为运行世界服务器分配足够的资源，因此需要创建一个新的交换空间。[此处可以找到该问题的各种解决方案。](https://askubuntu.com/questions/178712/how-to-increase-swap-space) 本指南将使用 `dd` [方法](https://askubuntu.com/a/178726)：

```Bash
#创建 3GB 的交换镜像并设置交换区域
sudo dd if=/dev/zero of=/media/fasthdd/swapfile.img bs=1024 count=3M
sudo mkswap /media/fasthdd/swapfile.img

#使用 sudo 权限在 /etc/fstab 打开编辑器
sudo nano /etc/fstab

# 将这一行添加到 /etc/fstab
/media/fasthdd/swapfile.img swap swap sw 0 0

#激活交换镜像
swapon /media/fasthdd/swapfile.img
```

### 连接到服务器

使用 `aws ec2 describe-instances` 查找实例的公共 IP 地址。将 `PublicIpAddress` 填入你的 `acore_auth` realmlist 表中。更多连接信息可以在[此处](http://www.azerothcore.org/wiki/Installation#8-connecting-to-the-server)找到。

------

## 免责声明

为了保持指南简洁，同时也出于对互联网安全的一般性认知不足，许多最佳实践并未遵循。如果计划允许任何人访问你的服务器，以下是一些需要了解并应该做到的事项：

- [为任何需要 AWS 访问权限的人添加 IAM 用户。](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) *不要允许某人运行 100 个实例去挖比特币……请记住，创建账号时会存储支付信息，而且 AWS 按使用的服务器小时数收费！* **请注意安全。**
- AWS 免费套餐允许 **750** 个实例小时，即 750/24 = 31.25 天。*一个月内只能不间断运行一个实例而无需付费，且免费套餐仅在账号创建后的 12 个月内有效。不要产生意外费用。你已经得到警告了！*
- 一般来说，在了解如何加固 Linux 安全之前，不要授予其他用户 SSH 或管理员权限，也不要授予任何人 root 权限。只给用户分配所需的最低权限。你的安全掌握在自己手中，祝你好运！
