# GDS Installation on Windows

1\. Create the following empty folder on the C: drive:

* C:\GDSStorage

2\. Download and install **Docker Desktop** ([https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/))

3\. Open a **Command Prompt**

4\. Create the _mywai_ network (if not yet created installing the Edge and Algo containers):

```batch
docker network create -d bridge --subnet=192.168.5.0/24 mywai
```

5\. Login into _mywai_ docker registry:

{% code overflow="wrap" %}
```batch
docker login -u mywai-pull -p <token> productfeatures.azurecr.io
```
{% endcode %}

{% hint style="warning" %}
Contact MYWAI to get the access token for the proper registry.\
The registry mywaik8sfeature.azurecr.io provides a more stable version of the Edge but not the very last one available. If you need the more up-to-date version, ask MYWAI for the access to the mywaik8snextdev.azurecr.io registry.
{% endhint %}

6\. Download the latest version of the docker images:

```batch
docker pull productfeatures.azurecr.io/gds:latest
```

7\. Create & Start the container, setting in the command below these environment variables:

* `IotHub__server`**:** the IP address or hostname of the IotHub service of the MYWAI Platform to be attached with.
* `IotHub__gdsId`**:** an unique identifier of you choice for your GDS. Only alphanumerical characters, dash and underscore are allowed.
* `GDS__gdsName`**:** a display name for your GDS.
* `GDS__gdsDescription`**:** a textual description of your GDS.
* `GDS__password`**:** a random password of your choice to secure the GDS access for application registrations. This security is used only to reduce the access for external registration requests of new Edges or Equipments, and is not used for normal operations.\
  You'll need to configure the same password for the Edge installations

```batch
docker run -d --name mywai-gds --restart always ^
--network mywai ^
--ip 192.168.5.4 ^
-p 8023:8023 ^
-p 58810:58810 ^
-v C:\GDSStorage:/GDSStorage ^
-e IotHub__server=<mywai-iothub-host> ^
-e IotHub__gdsId=<my-gds-id> ^
-e GDS__gdsName="<my-gds-name>" ^
-e GDS__gdsDescription="<my-gds-description>" ^
-e GDS__password="<my-gds-password>" ^
productfeatures.azurecr.io/gds:latest
```

{% hint style="warning" %}
The syntax shown above applies to Command Prompt. In PowerShell, the syntax differs and must be adjusted accordingly.
{% endhint %}
