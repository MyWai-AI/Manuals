# Data Import

The system allow to import these type of external data:

| Target                                      | Data type | Dimension                                        |
| ------------------------------------------- | --------- | ------------------------------------------------ |
| Equipment                                   | Events    | Multi sensor / field                             |
| Sensor                                      | Raw data  | Multi measure                                    |
| Blob (image, video, audio, csv time-series) | Raw data  | Raw blob files, no measure categorization needed |

## Events data format

This data format is a **ZIP** file that includes at least a **CSV** file that must be named "**events.csv**".

The import must be done selecting a single target Equipment on which to store the data, so all the data included must be belonging to an unique equipment element in the platform (being real or virtual).

The expected columns of the events.csv depends on the equipment configuration, in term of Equipment Type and Sensors attached.

The following example shows the content of a ZIP file for an Equipments that comes with a static field \<FIELD1>, a camera sensor \<CAMERA1>, a video sensor \<VIDEO1>, a temperature and salinity measures \<TEMP> and \<SALINITY>.

The columns TIMESTAMP and SERIAL\_NUMBER are fixed.

The column separator character must be the **semicolon** (;).

The name of the other columns that are enclosed in <> depends on actual **Sensor Names** or **Field Names** of the equipment.

The inner CSV files (imgs.csv and temp.csv in this example) must not have the header line and, in case of multi-measure and multi-field measure, must contain the different measure and field values in the proper order.

<figure><img src="../.gitbook/assets/image (20).png" alt=""><figcaption><p>An example of the ZIP file that represents Events to be imported in the Platform.</p></figcaption></figure>

## Raw data format
