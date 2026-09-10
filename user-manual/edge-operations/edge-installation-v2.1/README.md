# Edge Installation (v2.1)

The MYWAI Edge device runs in the company sites together with equipments, sensors and OPC servers to:

* Collect data
* Run AI Algorithms
* Trigger outcomes and alarms
* Execute orchestration flows

## System Requirements

MYWAY Edge runs on:

* Microsoft Windows devices: Windows 10 or 11.
* Linux devices with Ubuntu 22.04.
* Raspberry PI 4.

The entire Edge is provided as a Docker image. Please ensure to get the proper image for the selected SO.

## Installation Procedures

Please following the following procedures to install the Edge software on the specific devices:

* [Windows 10 or 11](installation-on-windows.md)
* [Ubuntu 22.04](installation-on-ubuntu.md)
* [Raspberry PI 4](installation-on-raspberry-pi-4.md)

## Offline Configuration Procedure

In cases where the Edge device operates in stand-alone mode, not connected to the Platform, it needs to be configured manually using the following procedure:

1. Download the json configuration file from the Platform: go on the Edges list page, click on the Details button on the Edge you want to manually configure and then click on the Download Edge Configuration button. A .json file will be downloaded with name`edge_config_<edge_id>.json`
2. Copy the file in the `EdgeStorage`folder on the Edge machine.
3. Install Mosquitto on the Edge host machine.
4. Run the following command from the host machine, replacing:\
   `[EdgeId]` with the local IP address of the Edge container\
   `[Config file name]` with the name of the file downloaded from the previous step\
   `[MQTTUsername]` the username to log in into MQTT server. The default value is "edge". The actual value can be found in the Edge appSettings.json file.\
   `[MQTTPassword]` the password to access the MQTT server. The actual value can be found in the Edge appSettings.json file.\
   \
   On Windows, the path to be provided in the -m parameter must start with "C:\EdgeStorage\\\[Config file name]".

```
mosquitto_pub -h [EdgeIp] -p 8883 -t UpdateConfigurationFromFileSystem -m "/EdgeStorage/[Config file name]" -u [MQTTUsername]-P [MQTTPassword]

```



