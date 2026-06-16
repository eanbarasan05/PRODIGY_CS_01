
# Caesar Cipher Program

def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


print("===== Caesar Cipher =====")
message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

print("\nChoose an option:")
print("1. Encrypt")
print("2. Decrypt")

choice = input("Enter your choice (1/2): ")

if choice == "1":
    encrypted_text = encrypt(message, shift)
    print("Encrypted Message:", encrypted_text)

elif choice == "2":
    decrypted_text = decrypt(message, shift)
    print("Decrypted Message:", decrypted_text)

else:
    print("Invalid choice!")
