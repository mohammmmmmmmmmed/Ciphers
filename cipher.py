text = 'mrttaqrhknsw ih puggrur'
ctext = 'Hello World'
custom_key = 'python'
shift = 3
def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        if not char.isalpha():
            final_message += char
        else:        
            key_char = key[key_index % len(key)]
            key_index += 1

            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def caesar(message, offset, direction=1):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            encrypted_text += alphabet[new_index]
    return encrypted_text

caesarText = caesar(ctext, shift)
print('Encrypted Caeser text: ' + caesarText)
plainCText = caesar(caesarText, shift, -1) 
print('Decrypted Caeser text: ' + plainCText)

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

print(f'\nVigenere Encrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nVigenere Decrypted text: {decryption}\n')