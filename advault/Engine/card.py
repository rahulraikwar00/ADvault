

from Crypto.Cipher import AES
from Crypto import Random
import json
import binascii

class Card:

    def __init__(self, key, details=""):
        self.details = details
        self.iv = Random.new().read(AES.block_size)
        self.key = key
        self.aes_obj = AES.new(self.key, AES.MODE_CFB, self.iv)

    def strip(self, string):
        _str = string
        _x = 0
        for x in _str:
            if(x == '"'):
                break
            else:
                _x += 1
        return _x

    @property
    def encrypt_data(self):
        _en_data = self.iv + self.aes_obj.encrypt(json.dumps(self.details).encode("utf-8"))
        return binascii.hexlify(_en_data).decode('utf-8').strip()

    def decrypt_data(self, ciphertext):
        ciphertext = ciphertext.encode('utf-8')
        ciphertext = binascii.unhexlify(ciphertext)
        data = self.aes_obj.decrypt(ciphertext).decode('ISO-8859-1')
        offset = self.strip(data)

        return data[offset:]

'''if __name__ == '__main__':

    key = "7195bb5c30deff29d83ac52b570b8c65"
    details = {'aadhaarno':'234-2788-98987','name':'mohd shibli','dob':'27-09-1997'}
    card = Card(key.encode("utf-8"), str(details))
    cipher = card.encrypt_data
    print(cipher)
    print("-------------------------------------------")
    print(Card(key.encode("utf-8")).decrypt_data(cipher))'''
