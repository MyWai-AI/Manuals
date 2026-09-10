# Configuration

For an Equipment, in general you have only Equipment Type Fields if the equipment exposes an OPC-UA Server, and youn have only Sensors if not. You can still use a mixed approach, so some fields from OPC-UA server and some data gathered with other data protocols using Sensors.Within this section we will cover the Configuration of your system, that will include the configuration of the following entities:

* **Equipment Types**\
  The list of the equipment types is the first step for your configuration. An Equipment Type collect the basic characteristics of similar Equipments.
* **Equipments**\
  An equipment represents a real device in your factory, with an unique identifier and a serial number, ad it is associated to an Equipment Type.
* **Measures**\
  A measure is defined by the type (acceleration, image, temperature...) and can be associated to a Sensor or directly to a Custom Fields
* **Sensors**\
  A sensor is a physical or virtual device that reads a measure.
* **Edge devices**\
  An Edge device is a physical computing device installed inside the factory, aside the equipments and sensors connected to him. It must run the MYWAY software.
* **Custom Fields**\
  You can define additional custom fields for Users and Sensors to enrich their anagraphic information.

## Typical configuration Workflow

This workflow describes the standard procedure to enable a new **Equipment**, from defining its **Measures** to associating it with an **Edge device**.

### **1. Measures**

Define the **measures** required for your equipment.\
The platform includes several predefined measures such as **Temperature**, **Acceleration**, **Pressure**, and **Image**. You can use these built-in measures or create new ones specific to your equipment.

### **2. Sensors**

If your equipment’s data is **not** available through an OPC UA Server, you need to configure **Sensors**.\
Sensors allow data collection from alternative sources such as:

* Local file systems
* HTTP/HTTPS servers
* Bluetooth devices

If all required data is exposed by the equipment’s **OPC UA Server**, you don’t need Sensors.

### **3. Equipment Type**

Define the **Equipment Type**.\
This allows you to deploy multiple instances of similar equipment efficiently.\
The core elements of an Equipment Type are the **Fields**, which:

* Represent individual data points or variables
* Will be the connection between an OPC UA Node and a Measure

### **4. Equipment**

Create the **Equipment** based on the defined Equipment Type.\
After creation, complete the following steps:

1. **Associate Sensors** (if required) created in step 2.
2. **Map each Field** from the Equipment Type to the corresponding OPC UA Node (refer to your equipment’s documentation to identify Node IDs) and to the corresponding Measure.\
   You can have several Fields for the same measure. For example, if an equipment provides 10 values of different temperatures, you will have 10 different Fields in the Equipment Type, all these associated to the Temperature measure.
3. **Set the OPC UA Server URL** for the equipment.

### **5. Edge association**

Associate the **Equipment** with an **Edge device** to start collecting and transmitting data.

#### Notes

* If the equipment exposes an OPC UA Server, it typically uses only **Equipment Type Fields**.
* If the equipment does **not** expose an OPC UA Server, it relies solely on **Sensors**.
* A **hybrid configuration** is also possible, combining both:
  * OPC UA fields for some data
  * Sensors for data collected via other protocols.

