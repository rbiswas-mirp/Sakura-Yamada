import base64

def encode_message(message):
    return base64.b64encode(message.encode()).decode()

def decode_message(encoded):
    return base64.b64decode(encoded).decode()
