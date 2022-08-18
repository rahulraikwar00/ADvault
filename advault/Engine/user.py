
import hashlib
import time
import sys
import binascii


class User:
    def __init__(self, user_details):
        self.user_details = user_details
        self.hash = hashlib()

    @property
    def generate_key(self):
        _name = self.user_details["name"]
        _nonce = str(int(time.time()))
        _token_value = _name + _nonce
        self.hash.update(_token_value.encode("utf-8"))
        return binascii.hexlify(self.hash.digest()).decode("utf-8")


class Democrypt:
    def __init__(self):
        pass
    def encrypt(self, data):
        return data + "encrypted"

    def decrypt(self, data):
        return data + "decrypted"


"""if __name__ == '__main__':
    details = {
        "name" : "Dante",
        "email" : "foo@bar.com"
    }

    user = User(details)
    print(len(user.generate_key))
    sys.stdout.write(user.generate_key+"\n")"""
