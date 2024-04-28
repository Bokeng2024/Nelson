def compare_binary_strings(str1, str2):
    """
    Compares two binary strings and returns "0" if they are equal, otherwise "1".
    Args:
        str1 (str): First binary string.
        str2 (str): Second binary string.
    Returns:
        str: "0" if str1 and str2 are equal, otherwise "1".
    """
    if str1 == str2:
        return "0"
    else:
        return "1"

# Example usage
binary_str1 = "101010"
binary_str2 = "101010"
result = compare_binary_strings(binary_str1, binary_str2)
print(f"Comparison result: {result}")

def encrypt_message(message, keystream):
    # Ensure the keystream is long enough to cover the entire message
    if len(keystream) < len(message):
        raise ValueError("Keystream must be at least as long as the message")

    # Initialize an empty list to store the encrypted characters
    encrypted_chars = []

    # Iterate over each character in the message
    for i in range(len(message)):
        # Get the ASCII value of the current character in the message
        message_char = ord(message[i])

        # Get the ASCII value of the corresponding character in the keystream
        keystream_char = ord(keystream[i])

        # Calculate the encrypted character by XOR-ing the message and keystream values
        encrypted_char = message_char ^ keystream_char

        # Append the encrypted character to the list
        encrypted_chars.append(chr(encrypted_char))

    # Join the list of encrypted characters into a single string
    encrypted_message = "".join(encrypted_chars)

    return encrypted_message

def encrypt_message(message, keystream):
    # Calculate the number of blocks needed
    num_blocks = len(message) // len(keystream)
    
    # Initialize the encrypted message
    encrypted_message = ""
    
    # Iterate over each block
    for i in range(num_blocks):
        # Get the current block of the message
        block = message[i * len(keystream): (i + 1) * len(keystream)]
        
        # XOR the block with the keystream
        encrypted_block = "".join(str(int(a) ^ int(b)) for a, b in zip(block, keystream))
        
        # Append the encrypted block to the result
        encrypted_message += encrypted_block
    
    # If the message length is not a multiple of keystream length, pad the last block with "0"
    if len(message) % len(keystream) != 0:
        last_block = message[num_blocks * len(keystream):]
        last_block += "0" * (len(keystream) - len(last_block))
        encrypted_message += "".join(str(int(a) ^ int(b)) for a, b in zip(last_block, keystream))
    
    return encrypted_message

# Example usage
message = "10101100110110"
keystream = "1011"
encrypted_message = encrypt_message(message, keystream)
print(f"Encrypted message: {encrypted_message}")
