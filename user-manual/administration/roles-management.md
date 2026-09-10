# Roles Management

## **Understanding Roles**

In the MYWAI platform, roles serve a pivotal purpose – they offer a structured way to assign specific permissions to users. By creating and assigning roles, administrators can ensure that users have the necessary access to perform their tasks while maintaining a secure and organized environment.

### **Key Characteristics of Roles**

1. **Unique role name:** Every role on the platform must have a unique name, ensuring clarity and preventing overlap or confusion.
2. **Permissions Assignment:** Each role is associated with a set of permissions that dictate the specific actions a user with specific roles can perform.
3. **Site and Area Specificity:** Roles can be further refined by associating them with specific sites and areas. This means that the permissions linked to a role will only be activated for entities assigned to the designated sites or areas. For instance, a user with a "Site Manager" role for "Site A" won't have the same permissions for "Site B" unless explicitly assigned.

## **The Roles Page**

Upon navigating to the Roles page, you will be presented with a list of all the roles configured within the system. Default roles such as, "Admin" and "User", are automatically included, serving general administrative and basic user functionalities, respectively.

**Capabilities of the Roles Page:**

1. **Create Roles:** To create a new role:
   * Click on the 'Add Role' button.
   * Provide a unique name for the role.
   * Select the permissions you wish to assign to the role.
   * Optionally, specify sites and areas where the role's permissions will be applicable.
   * Save the role.
2. **Edit Roles:** Existing roles (except default roles) can be modified to change their name, permissions set, or associated sites and areas. To do so:
   * Locate the role you wish to modify in the list.
   * Click on the 'Edit' button next to the role.
   * Make the necessary changes.
   * Save the updated role.
3. **Delete Roles:** If a role is no longer needed, it can be removed. However, take caution when doing so by making sure that users associated with that role do not lose critical access. To delete a role:
   * Find the role in the list.
   * Click on the 'Delete' button next to the role.
   * Confirm the deletion in the prompted dialogue box.

## List of Permissions

This is the complete list of Permissions that can be assigned to Roles:

| Permission name              | Meaning                                                                               |
| ---------------------------- | ------------------------------------------------------------------------------------- |
| Edit company information     | Allow to modify the details of the company                                            |
| View users                   | Allow to view all users registered on the platform and their roles                    |
| Manage users                 | Allow to create, edit or remove users and assign roles                                |
| View user roles              | Allow to view all roles                                                               |
| Manage user roles            | Allow to create, edit or remove roles, and assign them to sites and permissions       |
| View equipment               | Allow to view all equipment                                                           |
| Manage equipment             | Allow to create, edit or remove an equipment                                          |
| View equipment data analysis | Allow to view the data analysis for each equipment                                    |
| Deploy on edge               | Allow user to deploy algorithm and model to edge                                      |
| View sensors                 | Allow to view all sensors                                                             |
| Manage sensors               | Allow to create, edit or remove sensors and assign them to equipment and sites        |
| View custom fields           | Allow to view all custom field for equipment, sensors and users                       |
| Manage custom fields         | Allow to create, edit or remove custom fields to be used on equipment, sensors, users |
| View alarms                  | Allow to view alarms                                                                  |
| Manage alarms                | Allow to create, edit or remove alarms                                                |
| View algorithms              | Allow to view all algorithms                                                          |
| Manage algorithms            | Allow to create, edit or remove algorithm                                             |
| View labels                  | Allow to view all label                                                               |
| Manage labels                | Allow to create, edit or remove label                                                 |
| Label Review                 | Allow to discuss, accept, or reject label approval requests                           |
| View models                  | Allow to view model approval requests                                                 |
| Manage models                | Allow to to create, edit or remove approval requests                                  |
| Model Review                 | Allow to discuss, accept, or reject model approval requests                           |
| View Reports                 | Allow to view all algorithms                                                          |
| Manage Reports               | Allow to manage all algorithms                                                        |
| View edges                   | Allow to view all Edges                                                               |
| Manage edges                 | Allow to create, edit or remove edge                                                  |
| View anomalies               | Allow to view all anomalies                                                           |
| Manage anomalies             | Allow to create, edit or remove anomalies                                             |
| View routines                | Allow to view routines                                                                |
| Manage routines              | Allow to view routines                                                                |
| View rois                    | Allow to view rois                                                                    |
| Manage rois                  | Allow to view rois                                                                    |
| Execute algorithm            | Allow to train, execute algoorithm                                                    |
| View EquipmentType           | Allow view all equipment type                                                         |
| Manage EquipmentType         | Allow to create, edit or remove an equipment type                                     |
| View Measure                 | Allow to view all Measure                                                             |
| Manage Measure               | Allow to create, edit or remove an equipment                                          |
| View Certifications          | Allow to view certifications done                                                     |
| Manage Certifications        | Allow to view certifications done                                                     |
| Manage Orchestrator Flow     | Allow to manage orchestrator flow                                                     |
| View Orchestrator Flow       | Allow to view orchestrator flow                                                       |

## **In Conclusion**

Effective role management is fundamental for maintaining a structured and secure environment within the MYWAI platform. By understanding how roles, permissions, sites, and areas interplay, administrators can ensure that users have precise access levels tailored to their responsibilities. Always review and update roles periodically to align with the organization's evolving hierarchy.
