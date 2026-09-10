# GDS Installation on Ubuntu with Docker Compose

1. Create the following empty folder on the root:
   * /GDSStorage
2. Install **Docker Engine** following the official Docker installation guide for Ubuntu:\
   https://docs.docker.com/engine/install/ubuntu/

{% hint style="info" %}
Optionally consider to apply post-install settings for your Docker: [https://docs.docker.com/engine/install/linux-postinstall](https://docs.docker.com/engine/install/linux-postinstall). If you choose to use Docker as non-root user, omit "sudo" in all the following commands of this procedure.
{% endhint %}

3. After installation, ensure Docker is running:

```bash
sudo systemctl start docker
sudo systemctl enable docker
```

4\. Create the `mywai` Docker network (if not already created by other MYWAI containers):

```bash
sudo docker network create -d bridge --subnet=192.168.5.0/24 mywai
```

5\. Log in to the MYWAI Docker registry:

{% code overflow="wrap" %}
```bash
sudo docker login productfeatures.azurecr.io -u mywai-pull -p <token>
```
{% endcode %}

{% hint style="warning" %}
Contact MYWAI to get the access token for the proper registry.\
The registry mywaik8sfeature.azurecr.io provides a more stable version of the Edge but not the very last one available. If you need the more up-to-date version, ask MYWAI for the access to the mywaik8snextdev.azurecr.io registry.
{% endhint %}

6\. Create a file `.env` in the folder `/GDSStorage` where you will define the following environment variables as described below:

```
MYWAI_IOTHUB_SERVER=<value>
MYWAI_GDS_ID=<value>
MYWAI_GDS_NAME=<value>
MYWAI_GDS_DESCRIPTION=<value>
MYWAI_GDS_PASSWORD=<value>
```

* `MYWAI_IOTHUB_SERVER`**:** the IP address or hostname of the IotHub service of the MYWAI Platform to be attached with.
* `MYWAI_GDS_ID`**:** an unique identifier of you choice for your GDS. Only alphanumerical characters, dash and underscore are allowed.
* `MYWAI_GDS_NAME`**:** a display name for your GDS.
* `MYWAI_GDS_DESCRIPTION`**:** a textual description of your GDS.
* `MYWAI_GDS_PASSWORD`**:** a random password of your choice to secure the GDS access for application registrations. This security is used only to reduce the access for external registration requests of new Edges or Equipments, and is not used for normal operations.\
  You'll need to configure the same password for the Edge installations.

7. Create a file `docker-compose.yml` in the folder `/GDSStorage` with the following content:

```yaml
name: mywai

services:
  mywai-gds:
    image: productfeatures.azurecr.io/gds:latest
    container_name: mywai-gds
    restart: always
    networks:
      mywai:
        ipv4_address: 192.168.5.4
    ports:
      - "8023:8023"
      - "58810:58810"
    volumes:
      - /GDSStorage:/GDSStorage
    environment:
      IotHub__server: ${MYWAI_IOTHUB_SERVER}
      IotHub__gdsId: ${MYWAI_GDS_ID}
      GDS__gdsName: ${MYWAI_GDS_NAME}
      GDS__gdsDescription: ${MYWAI_GDS_DESCRIPTION}
      GDS__password: ${MYWAI_GDS_PASSWORD}

networks:
  mywai:
    external: true
```

{% hint style="info" %}
192.168.5.4 is the default internal IP address of the GDS. Edge nodes automatically attempt to discover a local GDS at this address. If you change it, you must also configure any local Edge to explicitly specify the GDS address it should connect to. See [this section](../edge-installation-v3.0/advanced-installations.md#connect-edge-with-a-gds-on-a-different-device) for the details.
{% endhint %}

8. Run the following command from the folder `/GDSStorage`:

```shellscript
docker compose up -d
```
