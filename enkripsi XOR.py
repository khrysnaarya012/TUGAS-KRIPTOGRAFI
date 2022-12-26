print("|||||||||||||||||||||||||||||||||||||||")
print("||Nama : Ageng Arya Khrysna Dwipangga||")
print("||NIM  : E1E120056                   ||")
print("|||||||||||||||||||||||||||||||||||||||")
kunci = input('Masukkan Kunci: ')
byte_input = bytes(kunci, 'utf-8')
plaintext = input('Masukkan Plainteks: ')

encrypted_data = b''
encrypted_data.decode('biner')


for i, c in enumerate(plaintext):
    encrypted_data += bytes([ord(c) ^ byte_input[i % len(byte_input)]])
print('Enkripsi: ', encrypted_data.decode('utf-8'))


def decrypt(encrypted_text, kunci):
    decrypted_text = ""
    for i in range(len(encrypted_text)):
        decrypted_text += chr(ord(encrypted_text[i]) ^ ord(kunci[i % len(kunci)]))
    return decrypted_text


encrypted_text = encrypted_data.decode('utf-8')
decrypted_text = decrypt(encrypted_text, kunci)


print('Dekripsi: ', decrypted_text)