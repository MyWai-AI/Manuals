# Blockchain (v3.0)

You can use this page to configure the Blockchain for the Data Certification on **IOTA** Networks.

### **Supported Networks**

The platform supports both IOTA environments:

* **Testnet:**\
  Used for development and testing. No real-value tokens are required.\
  Recommended for non-production environments.
* **Mainnet:**\
  The production network used for permanent and verifiable certifications.\
  Transactions recorded here are immutable and publicly accessible through the official IOTA Explorer.

The active network can be selected directly from the **Blockchain** page in the platform interface.

### **Wallet Management**

From the **Blockchain** page, users can manage the wallet associated with their account.

**2.1 Create a New Wallet**

* The platform can generate a new **IOTA wallet** directly.
* A **mnemonic phrase** (typically 24 words) and corresponding **address** are automatically created.
* Once created, it is used to sign all certification transactions. In case Mainnet is selected, the walled need to be **funded** before starting to process transaction (see [Firefly](https://firefly.iota.org/)).

**2.2 Import an Existing Wallet**

* Users can import an existing IOTA wallet **from a mnemonic phrase**.
* The mnemonic must follow the BIP39-compatible format used by IOTA wallets.
* After import, the wallet is securely stored and immediately becomes the active signing wallet.

**2.3 View Wallet Status**

The Blockchain configuration page displays:

* Current wallet **address**
* Active **network** (Testnet or Mainnet)

<figure><img src="../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

### **Prerequisites for Certification**

Before performing any certification, ensure:

1. A valid **wallet** is created or imported.
2. The correct **network** (Testnet/Mainnet) is selected.
3. The wallet has sufficient **IOTA tokens** (only required for Mainnet).

Once these conditions are satisfied, manual data certification can be executed.

### Funding for mainnet

After having a **mainnet** wallet configured, here the steps to add real funds to the wallet:

* Use a crypto exchange or a broker, like [Binance](https://www.binance.com/), to purchase some MIOTA cryptos.
* Transfer the desired amount to your Wallet.
