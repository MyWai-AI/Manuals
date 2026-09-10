# Measures

## **Understanding Measures**

In the realm of technical data representation, a "Measure" serves as a structured definition, encapsulating a set of fields that together represent a particular kind of data or reading. Measures help standardize the data's presentation, ensuring that each field is recognized and interpreted in the correct context.

### **Key Components of a Measure**

1. **Unique Name:** Each Measure possesses a distinct name, ensuring clarity and eliminating potential ambiguities. The name cannot contains spaces.
2. **Fields:** These are the building blocks of a Measure. Every field is defined by:
   * **Name:** A descriptor for the data it represents. The name cannot contains spaces.
   * **Type:** Dictates the nature and format of data the field will hold. The available types are: smallint, integer, float, string, image, audio, and video.

### When to Differentiate Measures

Suppose you develop an algorithm that can operate on both **hydraulic** and **pneumatic** systems.\
Both systems provide a single floating-point value representing pressure. Structurally, they are identical:

| Measure  | Field Name | Type  |
| -------- | ---------- | ----- |
| Pressure | value      | float |

However, the **context** differs: one represents **hydraulic pressure**, the other **air pressure**.\
Creating two distinct Measures, for instance:

* `HydraulicPressure`
* `AirPressure`

allows algorithms to differentiate between them automatically, select appropriate processing logic, or apply domain-specific thresholds, without need to rely on equipment type fields that can have different names on different Equipments.

This distinction becomes essential when:

1. You run **shared analytics** or **AI models** across multiple equipment types.
2. You need to **filter** or **aggregate** data by its physical context.
3. You plan to **reuse** or **share** Measures across projects without ambiguity.

## **Measures Management Page**

The Measures Management page is your gateway to handle, define, and comprehend the various Measures in the system. Here's what you can accomplish on this page:

1. **Listing Existing Measures:** On accessing the page, you'll be presented with a comprehensive list of all existing Measures, allowing for a quick overview and easy navigation.
2. **Adding Measures:**
   * Click on the 'Add' or 'Create' button (usually located at the top or bottom of the list).
   * Fill in the unique name for the Measure.
   * Define the **fields** by providing their name and selecting the appropriate type from the available options.
   * Confirm or save the new Measure.
3. **Deleting Measures:** If a Measure is no longer required or was added erroneously:
   * Locate the desired Measure from the list.
   * Click on the 'Delete' or 'Remove' option (often represented with a trash bin icon).
   * Confirm the deletion, and the Measure will be removed from the system.

### Supported Field Types

Here the supported field types:

* Smallint
* Integer
* Float
* String
* Image
* Audio
* Video

{% hint style="warning" %}
Multiple fields are supported only for numeric and string types, so, Image, Audio and Video fields can be used only on single-field Measures.
{% endhint %}

### **Example - Acceleration Measure**

To illustrate the concept, consider the Measure "Acceleration." It comprises three distinct fields:

* **x:** A float value representing acceleration along the x-axis.
* **y:** A float value signifying acceleration along the y-axis.
* **z:** A float value detailing acceleration along the z-axis.

In summary, the Measures Management page is an instrumental tool, enabling users to consistently and accurately define the technical representations of various data types. By mastering this page, you ensure that the data fed into and interpreted by the system adheres to standardized and meaningful definitions.

###
