from chacha20poly1305 import ChaCha20Poly1305
import json
from hashlib import sha256
from time import time


class JsonCipher:
    """
    Wrapper class to use ChaCha20Poly1305 with json data ...
    Here should be more docs ...

    """
    def __init__(self, private_key):
        self.private_key = private_key
        self.cipher = ChaCha20Poly1305(sha256(private_key.encode("utf-8")).digest())
        self.current_nonce = ""
        self.previous_nonce = ""
        self.decrypt_data_success = False
        self.decrypted_data = {}

    def _generate_nonce(self):
        self.decrypt_data_success = False
        current_mixed_string = str(round(time() / 5)) + self.private_key
        previous_mixed_string = str(round(time() / 5)-1) + self.private_key
        self.current_nonce = sha256(current_mixed_string.encode("utf-8")).digest()[:12]
        self.previous_nonce = sha256(previous_mixed_string.encode("utf-8")).digest()[:12]

    def _decrypt_data_with_nonce(self, nonce, data):
        try:
            self.decrypted_data = json.loads(self.cipher.decrypt(nonce, data).decode("utf-8"))
            self.decrypt_data_success = True
        except:
            self.decrypt_data_success = False

    def encrypt_dict(self, data_to_encrypt):
        self._generate_nonce()
        return self.cipher.encrypt(self.current_nonce, json.dumps(data_to_encrypt).encode("utf-8"))

    def decrypt_dict(self, data_to_decrypt):
        self._generate_nonce()
        self._decrypt_data_with_nonce(self.current_nonce, data_to_decrypt)
        if self.decrypt_data_success:
            return self.decrypted_data
        else:
            self._decrypt_data_with_nonce(self.previous_nonce, data_to_decrypt)
        return {}
