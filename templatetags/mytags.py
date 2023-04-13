# myapp/templatetags/mytags.py
from django import template
import logging,traceback,base64
from cryptography.fernet import Fernet
register = template.Library()
from StressandAnxiety import settings
key=b'Cp-AAWHWkXClIJS-XokS9KTOtMxaw0pJWDh2lJqM1X4='
fernet = Fernet(key)
@register.filter
def keyvalue(dict, key):    
    return dict[key]
@register.filter
# def decrypt(encrypted):
#     try:
#         # base64 decode
#         txt = base64.urlsafe_b64decode(encrypted)
#         cipher_suite = Fernet(settings.ENCRYPT_KEY)
#         decoded_text = cipher_suite.decrypt(txt).decode("ascii")     
#         return decoded_text
#     except Exception as e:
#         # log the error
#         logging.getLogger("error_logger").error(traceback.format_exc())
#         return None
    # key = settings.ENCRYPT_KEY

    # # create a Fernet object with the key
    # fernet = Fernet(key)

    # # message to be encrypted
    

    # # encrypt the message
    

    # # decrypt the message
    # print(encrypted)
    # decrypted = fernet.decrypt(encrypted).decode("ascii")
    # return decrypted


# Create a Fernet object with the key


def decrypt(cipher_text):
    # Decrypt the cipher text
    print(key)
    plain_text = fernet.decrypt(cipher_text.encode())

    # Return the plain text
    return plain_text.decode()
