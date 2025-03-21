import json
from utils import encode_message

def main():
    with open('config.json') as config_file:
        data = json.load(config_file)

    message = data.get('secret', '')
    encoded_message = encode_message(message)
    print(f"Encoded Message: {encoded_message}")

if __name__ == "__main__":
    main()
