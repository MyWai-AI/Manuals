# Users management

To access the section dedicated to the user management, you can click on the "Users" entry located in the platform's navigation menu, found under the "Assets" section.

## Creating a User

When creating a new user on the platform, the system automatically takes care of generating a matching account on Auth0. This ensures that each user has a unique and secure profile to log into, leveraging Auth0's advanced functionalities in terms of security and identity management.

{% hint style="info" %}
If an account for a specific user is already present in the Auth0 system, the same account will be used. Therefore the user will be able to access all MYWAI tenants where they have been enrolled in using the very same account.
{% endhint %}

### User Identification

Each user within the platform is uniquely identified by the following details:&#x20;

* **Name**: The user's first name.
* **Surname**: The user's last name.
* **Email**: The email address associated with the user, also used for logging in.
* **Associated Roles**: A list of roles assigned to the user. These roles determine the functionalities and areas of the platform that a user can access.

{% hint style="info" %}
If you need more fields to identify your users, you can configure additional fields using the [custom-fields.md](custom-fields.md "mention")feature.
{% endhint %}

### Available Operations

From the user management page, you have the ability to:

**Add Users**: You can create a new user by providing the required details and assigning one or more roles to them. Once created, the user will receive an email notification containing the instructions to set their password and complete the registration procedure.

**Modify Users**: By selecting a user from the list, you can modify their details, such as name, surname, email, or associated roles.

**Remove Users**: If necessary, you can remove a user from the platform. Be cautious, this operation is irreversible and will result in the user's removal from Auth0 as well.
