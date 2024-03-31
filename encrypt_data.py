from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.keyvault.keys import KeyClient
from azure.keyvault.keys.crypto import CryptographyClient, EncryptionAlgorithm
import base64

# Azure Key Vault details
key_vault_uri = "https://kenanyusufskeyvault.vault.azure.net/"
key_name = "KenanLab5Key"

# The string to encrypt
plaintext = "Hello, Azure Key Vault!"

# Authenticate to Azure Key Vault for keys and secrets
credential = DefaultAzureCredential()
key_client = KeyClient(vault_url=key_vault_uri, credential=credential)
secret_client = SecretClient(vault_url=key_vault_uri, credential=credential)

# Retrieve the key to use for encryption
key = key_client.get_key(key_name)
crypto_client = CryptographyClient(key, credential)

# Encrypt the data
result = crypto_client.encrypt(EncryptionAlgorithm.rsa_oaep, plaintext.encode())
encrypted = result.ciphertext

# Convert encrypted data to a format that can be stored as a secret (base64)
encrypted_base64 = base64.b64encode(encrypted).decode("utf-8")

# Store the encrypted data as a secret
secret_name = "encryptedString"
response = secret_client.set_secret(secret_name, encrypted_base64)

# Display the encrypted data and secret information
print(f"Encrypted data: {encrypted_base64}")
print(f"Secret stored: {response.name}, with version: {response.properties.version}")

# Retrieve the encrypted data as a secret
retrieved_secret = secret_client.get_secret(secret_name)

# Decode the encrypted data from base64
encrypted_data_retrieved = base64.b64decode(retrieved_secret.value)

# Decrypt the data
decrypt_result = crypto_client.decrypt(EncryptionAlgorithm.rsa_oaep, encrypted_data_retrieved)
decrypted_data = decrypt_result.plaintext.decode("utf-8")

# Display the original (decrypted) string
print(f"Decrypted data: {decrypted_data}")
