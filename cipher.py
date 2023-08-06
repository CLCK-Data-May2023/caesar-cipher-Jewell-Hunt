def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = (ord(char) - ord('a') + shift) % 26 + ord('a')
            encrypted_text = encrypted_text + chr(shifted)
        else:
            encrypted_text = encrypted_text + char
    return encrypted_text

#predefined shift value
shift = 5

# Get user input
original_text = input("Enter the text to encrypt: ").lower()

encrypted_text = caesar_encrypt(original_text, shift)
print("The encrypted sentence is:", encrypted_text)