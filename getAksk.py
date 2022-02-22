import requests
import hmac
import base64,sys
from hashlib import sha1

ak = "your-ak"
sk = "your-sk"

HOST = "127.0.0.1:5201"
METHOD = "POST"
PATH = "/getToken"
CONTENT_TYPE = "application/json"
data= '{"flag":"test","appId":"001"}'

def sign():
    raw1 = "{} {}\n".format(METHOD, PATH)
    raw2 = "Host: {}\n".format(HOST)
    raw3 = "Content-Type: {}\n".format(CONTENT_TYPE)
    raw4 = "\n"
    # print(raw1)
    # print (raw2)
    # print (raw3)
    # print (raw4)
    # print (data)
    hmaccode = hmac.new(bytes(sk.encode('utf-8')),bytes("{}{}{}{}{}".format(raw1, raw2, raw3, raw4, data).encode('utf-8')),sha1).digest()
    b64code = base64.b64encode(bytes(hmaccode))
    # b64code = base64.b64encode(bytes(hmaccode.encode('utf-8')))
    b64code = b64code.decode().replace('/', '_').replace('+', '-')
    # print (11111,b64code)
    code = "mt {}:{}".format(ak,b64code)
    print ('"aksk":"{}"'.format(code))
    return code

if __name__ == "__main__":
    code=sign()