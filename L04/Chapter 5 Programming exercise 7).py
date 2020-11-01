# Chapter 5, programming exercise 7
# This program can encode and decode
# Caesar ciphers (a simple substitution
# cipher).

def main():
    plaintext_string = input("Enter the message you would like to encrypt: ")
    key = int(input("Enter the key value: "))

    # Encoding the message
    encoded_string = ""
    for x in plaintext_string:
        encoded_string += chr(ord(x) + key)

    print("Your encoded message is:", encoded_string)

    # Decoding
    decoded_string = ""
    for x in encoded_string:
        decoded_string += chr(ord(x) - key)
    
    print("Your decoded message is:", decoded_string)

main()