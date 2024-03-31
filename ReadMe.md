
# Encryption and Key Management with Azure Key Vault

## Setup of Azure Key Vault

### Creating the Key Vault

- **Navigation**: Accessed Azure Portal and navigated to "Create a resource" > "Key Vault".
- **Configuration**: Specified a unique name, selected a subscription, resource group, and region.
- **Review and Creation**: Reviewed the settings and created the Key Vault.
![Create Key Vault](Screenshots/create-key-vault.png "Creating Azure Key Vault")
![Key Vault Overview](Screenshots/key-vault-overview.png "Key Vault Overview")

### Setting Access Policies

- **Access Control**: Configured access policies to allow my account to manage keys and secrets.
- **Permissions**: Granted permissions for key and secret management, ensuring the application could encrypt, decrypt, store, and retrieve data.
![Role Assignment](Screenshots/Role-Assignment.png "Role Assignment in Azure Key Vault")

### Creating an Encryption Key

- **Key Generation**: Used Azure Key Vault to generate a new RSA key named `KenanLab5Key`.
- **Key Management**: Noted down the key identifier for use in the encryption and decryption process.
![Generate Key](Screenshots/Generate-Key.png "Generating a Key in Azure Key Vault")

## Encryption, Storage, Retrieval, and Decryption Processes

### Encrypting Data

- **Script Setup**: Installed necessary Azure SDK packages using `pip`.
- **Data Encryption**: Wrote a Python script that takes a plaintext string, encrypts it using the Azure Key Vault key, and displays the ciphertext.
![First Encryption Program](Screenshots/1st-encryption-program.png "First Encryption Program")
![Output of First Program](Screenshots/Output-of-1st.png "Output of First Encryption Program")

### Storing Encrypted Data

- **Secret Storage**: Modified the script to store the encrypted string as a secret in Azure Key Vault.
![Modified Encryption Program](Screenshots/Modified-encryption-program.png "Modified Encryption Program Code")
- **Confirmation**: Script outputs confirmation that the secret is stored, along with its identifier.
![Output of Modified Program](Screenshots/Output-of-modified-program.png "Output of Modified Encryption Program")


### Decrypting Data

- **Key and Secret Retrieval**: Script fetches the encryption key and the encrypted string (stored as a secret) from Azure Key Vault.
![Final Encryption Program](Screenshots/Final-Encryption-Program.png "Final Encryption Program Code")
![Final Encryption Program Part 2](Screenshots/Final-Encryption-Program-2.png "Final Encryption Program Code - Part 2")

- **Data Decryption**: Uses the fetched key to decrypt the string, displaying the original message to confirm successful decryption.
![Output of Final Program](Screenshots/Output-of-final-program.png "Output of Final Encryption Program")
![Output of Final Program Part 2](Screenshots/Output-of-final-program-2.png "Output of Final Encryption Program - Part 2")

## Challenges and Resolutions

- **Authentication Issues**: Encountered difficulties with the `DefaultAzureCredential` method, resolved by using the Azure CLI to log in with `az login`.
- **Permission Errors**: Initially received a `Forbidden` error when attempting to decrypt data. Resolved by adjusting the access policies in Azure Key Vault to include decrypt permissions for the application.
