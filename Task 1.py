def caesar_cipher(text, shift, mode):
    result = ""
    
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == "encrypt":
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == "decrypt":
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char  # Keep non-alphabet characters as-is
    return result

def main():
    print("Caesar Cipher Program")
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    message = input("Enter the message: ")
    try:
        shift = int(input("Enter the shift value (0-25): "))
        if not (0 <= shift <= 25):
            raise ValueError("Shift must be between 0 and 25.")
    except ValueError as e:
        print(f"Invalid shift value: {e}")
        return

    output = caesar_cipher(message, shift, mode)
    print(f"Result ({mode}ed): {output}")

if __name__ == "__main__":
    main()
