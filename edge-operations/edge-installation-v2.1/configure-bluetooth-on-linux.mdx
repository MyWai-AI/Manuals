# Configure Bluetooth on Linux

If you plan to use the Bluetooth adapters with a Linux Edge, you need to follow these instructions to properly configure the host machine.

1. Run the following commands to install the Bluetooth packages:

```bash
apt-get update
apt-get install -y bluez bluetooth
```

2. Configure the D-Bus using the root.conf file below. Replace, if differs from root, the user reported in `<policy user="root">` with the actual user you are using to run Docker, and then copy the file into the `/etc/dbus-1/system.d/`folder.

```xml
<!-- This configuration file specifies the required security policies
     for Bluetooth core daemon to work. 
     COPY ./pi.conf /etc/dbus-1/system.d/
     -->

<!DOCTYPE busconfig PUBLIC "-//freedesktop//DTD D-BUS Bus Configuration 1.0//EN"
 "http://www.freedesktop.org/standards/dbus/1.0/busconfig.dtd">
<busconfig>

  <!-- ../system.conf have denied everything, so we just punch some holes -->

  <policy user="root">
    <allow own="org.bluez"/>
    <allow send_destination="org.bluez"/>
    <allow send_interface="org.bluez.Agent1"/>
    <allow send_interface="org.bluez.MediaEndpoint1"/>
    <allow send_interface="org.bluez.MediaPlayer1"/>
    <allow send_interface="org.bluez.Profile1"/>
    <allow send_interface="org.bluez.GattCharacteristic1"/>
    <allow send_interface="org.bluez.GattDescriptor1"/>
    <allow send_interface="org.bluez.LEAdvertisement1"/>
    <allow send_interface="org.freedesktop.DBus.ObjectManager"/>
    <allow send_interface="org.freedesktop.DBus.Properties"/>
  </policy>

  <!-- allow users of bluetooth group to communicate -->
  <policy group="bluetooth">
    <allow send_destination="org.bluez"/>
  </policy>

  <policy at_console="true">
    <allow send_destination="org.bluez"/>
  </policy>

  <!-- allow users of lp group (printing subsystem) to 
       communicate with bluetoothd -->
  <policy group="lp">
    <allow send_destination="org.bluez"/>
  </policy>

  <policy context="default">
    <deny send_destination="org.bluez"/>
  </policy>

</busconfig>
```
