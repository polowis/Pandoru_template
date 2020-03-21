import base64
import os
from math import floor

def generate_nonce(length):
   """ Generates a random string of bytes, base64 encoded """
   if length < 1:
      return ''
   string=base64.b64encode(os.urandom(length),altchars=b'-_')
   b64len=4*floor(length)
   if length%3 == 1:
      b64len+=2
   elif length%3 == 2:
      b64len+=3
   return string[0:b64len].decode()