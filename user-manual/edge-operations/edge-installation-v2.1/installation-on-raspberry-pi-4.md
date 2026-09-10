# Installation on Raspberry Pi 4

To install Edge on a Raspberry Pi 4 follow these steps.

## Installing Docker on Raspberry Pi 4

To install Docker on your Raspberry Pi 4, ensure you're running a compatible OS, such as Raspbian Buster or later.

1.  **Update your system**:

    ```bash
    sudo apt update && sudo apt upgrade
    ```
2.  **Install Docker** using the convenience script from Docker:

    ```bash
    curl -sSL https://get.docker.com | sh
    ```

    This script will detect your architecture and install the appropriate Docker version.
3.  **Grant the `pi` user permission** to run Docker commands without `sudo`:

    ```bash
    sudo usermod -aG docker pi
    ```

    You'll need to either log out and back in or restart your Raspberry Pi for the group changes to take effect.
4.  **Verify the installation** by checking the Docker version:

    ```bash
    docker --version
    ```

## Install and configure the Edge Docker image

1. Import the "edge.tar" image in the device.
2. Run the following commands:

<pre class="language-bash" data-overflow="wrap"><code class="lang-bash">    sudo docker load --input edge.tar
<strong>    sudo docker create -p 1883:1883 -p 9001:9001 -p 8023:8023 -v /home/pi/EdgeIO:/EdgeIO --name edgecontainer --net mywai --ip 192.168.5.3 edge:latest -e IotHubAzure__ConnectionString=XXX -e IotHubAzure__EdgeID=MyEdge
</strong></code></pre>
