# Custom Fields

The platform offers the flexibility to create custom fields, providing an enhanced layer of detail to Users or Sensor records. These custom fields allow you to capture additional information tailored to your specific needs.

## **Defining a Custom Field**

To create a custom field, the following attributes must be specified:

1. **Category**: Determines the association of the custom field. It can be linked to:
   * Users
   * Sensors
   * Both Users and Sensors
2. **Name**: A unique identifier for the custom field. This name is mandatory and should succinctly describe the nature of the information being captured.
3. **Type**: Represents the kind of data the custom field will hold. Available types are:
   * String
   * Number
   * Boolean
   * Date
   * List
4. **Mandatory Flag**: This flag specifies whether the entry of information in the custom field is obligatory. If set, the field cannot be left blank for any User or Sensor it's associated with.

**Usage**

Once a custom field is defined, it seamlessly integrates into the respective anagraphic forms for Users or Sensors. For fields marked as mandatory, any new or updated record will require an entry in the custom field before it can be saved.

**Benefits**

By harnessing the power of custom fields, organizations can tailor MYWAI's platform to better suit their unique requirements, ensuring that the data most pertinent to them is always at their fingertips.
