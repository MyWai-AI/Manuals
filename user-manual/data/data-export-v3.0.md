# Data Export (v3.0)

## Exporting equipment information in AASX format

Starting from the v3.0 of the platform you can export your equipment in AASX format (**Asset Administration Shell Package**).

The package will include the following information:

* **Equipment metadata**
  * Name
  * Description
  * Image
  * Video
  * 3D Model
* **Extended AASX data**\
  These extended data are made available as a Type in the Equipment Types page named "**AASX Info**". To be able to enter these data, attach this node as a direct child of the Equipment Type of your equipment. This equipment type section includes the following additional fields:
  * ManufacturerName
  * URIOfTheProduct
  * YearOfConstruction
  * ManufacturerProductFamily
  * ContactInformation
    * Street
    * Zipcode
    * CityTown
    * NationalCode
  * ...more fields will be defined in the final release of the 3.0 version.
* Optionally, all **documents** associated to the equipment.
* Optionally, an example of **equipment data** on a specific time range you can define during the export.

From a technical perspective, these are the standard SubModule used to host these data inside the AASX:

* IDTA 02004-1-2  &#x20;Handover  &#x20;Documentation\
  [https://industrialdigitaltwin.org/en/wp-content/uploads/sites/2/2023/03/IDTA-02004-1-2\_Submodel\_Handover-Documentation.pdf](https://industrialdigitaltwin.org/en/wp-content/uploads/sites/2/2023/03/IDTA-02004-1-2_Submodel_Handover-Documentation.pdf)
* IDTA 02006-2-0  &#x20;Digital Nameplate for  &#x20;Industrial Equipment\
  [https://industrialdigitaltwin.org/en/wp-content/uploads/sites/2/2022/10/IDTA-02006-2-0\_Submodel\_Digital-Nameplate.pdf](https://industrialdigitaltwin.org/en/wp-content/uploads/sites/2/2022/10/IDTA-02006-2-0_Submodel_Digital-Nameplate.pdf)
* IDTA-02008-1-1 Time Series Data\
  [https://industrialdigitaltwin.org/wp-content/uploads/2023/03/IDTA-02008-1-1\_Submodel\_TimeSeriesData.pdf](https://industrialdigitaltwin.org/wp-content/uploads/2023/03/IDTA-02008-1-1_Submodel_TimeSeriesData.pdf)

