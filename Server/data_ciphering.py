from chacha20poly1305 import ChaCha20Poly1305
import json
from time import time


class DataCiphering:
    """
    Wrapper class to use ChaCha20Poly1305 ciphering with json data format. This class allow to easy encrypt and
    decrypt data with automatically generated nonce.
    """

    def __init__(self, private_key):
        """
        Create ciphering object which is responsible for all ciphering operation on data. Decrypting data demands
        generating two nonce's because probability that generated nonce had to late time base and decryption fails
        therefore provided key was appropriate.

        :param private_key: security access key
        """
        self.private_key = str(private_key)
        self.cipher = ChaCha20Poly1305(private_key)
        self.current_nonce = ""
        self.previous_nonce = ""
        self.decrypt_data_success = False
        self.decrypted_data = {}
        self.input_data_to_encrypt = {}

    def _generate_nonce(self):
        """
        Generates unique nonce based on real time and private key using sha256 hashing algorithm.

        :return: None
        """
        self.decrypt_data_success = False
        current_mixed_string = str(round(time() / 5)) + self.private_key
        previous_mixed_string = str(round(time() / 5) - 1) + self.private_key
        self.current_nonce = current_mixed_string.encode("utf-8")[:12]
        self.previous_nonce = previous_mixed_string.encode("utf-8")[:12]

    def _decrypt_data_with_nonce(self, nonce, data):
        """
        Decrypt provided data and give feedback about result of this action.

        :param nonce: nonce generated with appropriate method
        :param data: input data to decrypt
        :return: None
        """
        try:
            self.decrypted_data = json.loads(self.cipher.decrypt(nonce, data).decode("utf-8"))
            self.decrypt_data_success = True
        except:
            self.decrypt_data_success = False

    def _check_data_format(self):
        if type(self.input_data_to_encrypt).__name__ == "dict":
            return self.input_data_to_encrypt
        else:
            return {"data": str(self.input_data_to_encrypt)}

    def encrypt_dict(self, data_to_encrypt):
        """
        Encrypt provided dictionary with appropriate nonce.

        :param data_to_encrypt: input data to encrypt
        :return:
        """
        self._generate_nonce()
        self.input_data_to_encrypt = data_to_encrypt
        return self.cipher.encrypt(self.current_nonce, json.dumps(self._check_data_format()).encode("utf-8"))

    def decrypt_dict(self, data_to_decrypt):
        """
        Decrypt provided dictionary with appropriate nonce. This method in in first step try to decrypt data with
        current nonce and next if fails try to decrypt with previous nonce.

        :param data_to_decrypt: input data to decryption in dictionary format
        :return:
        """
        self._generate_nonce()
        self._decrypt_data_with_nonce(self.current_nonce, data_to_decrypt)
        if self.decrypt_data_success:
            return self.decrypted_data
        else:
            self._decrypt_data_with_nonce(self.previous_nonce, data_to_decrypt)
        return {}
