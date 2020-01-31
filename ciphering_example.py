from chacha20poly1305 import ChaCha20Poly1305
import json
from hashlib import sha256
from time import time

# ----------------------------------------------------- ENCRYPTING
message = {
    'action': "get_data_from_sensor"
}

json_message = json.dumps(message)

utf_8_encoded_message = json_message.encode("utf-8")

security_key = "tajny_klucz"

utf_8_encoded_security_key = security_key.encode("utf-8")

sha_256_digested_security_key = sha256(utf_8_encoded_security_key).digest()

cipher_object = ChaCha20Poly1305(sha_256_digested_security_key)

unix_time_in_seconds_divided_by_5_in_string_format = str(time() / 5)

mixed_string = unix_time_in_seconds_divided_by_5_in_string_format + security_key

utf_8_encoded_mixed_string = mixed_string.encode("utf-8")

sha_256_digested_mixed_string = sha256(utf_8_encoded_mixed_string).digest()

nonce = sha_256_digested_mixed_string[:12]

cipher_message = cipher_object.encrypt(nonce, utf_8_encoded_message)

print("Message before ciphering:\n\n")
print(message)
print("\n")
print("Message after ciphering: \n\n")
print(cipher_message)
print("\n")

# ----------------------------------------------------- DECRYPTING

decrypted_message = cipher_object.decrypt(nonce, cipher_message)

utf_8_decoded_decrypted_message = decrypted_message.decode("utf-8")

json_decrypted_message = json.loads(utf_8_decoded_decrypted_message)

print("Message after decrypting: \n\n")
print(json_decrypted_message)
print("\n")
