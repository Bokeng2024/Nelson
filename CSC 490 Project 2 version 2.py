import random

def shift(register):
    """
    Shifts the register state by one clock cycle.
    """
    # XOR the first and last bits
    new_bit = register[0] ^ register[-1]
    # Shift all bits to the right
    shifted_register = [new_bit] + register[:-1]
    return shifted_register

def generate_keystream(s, n):
    """
    Generates the keystream after n clock cycles.
    
    Args:
        s (str): String representing the initial state of the register.
        n (int): Number of clock cycles.
    
    Returns:
        list: Keystream as a list of 0s and 1s.
    """
    # Initialize the register state
    register = [int(bit) for bit in s]
    keystream = []

    for _ in range(n):
        # Generate a random input for the register
        input_bit = random.randint(0, 1)
        # Update the register state
        register = shift(register)
        # XOR the output bit with the input bit
        output_bit = register[-1] ^ input_bit
        # Append the output bit to the keystream
        keystream.append(output_bit)

    return keystream

# Example usage
initial_state = "101010"
clock_cycles = 10
keystream_output = generate_keystream(initial_state, clock_cycles)
print(f"Keystream after {clock_cycles} clock cycles: {keystream_output}")
def shift(s, rin):
    # Remove the leftmost bit from the register state
    s = s[1:]
    # Append the input bit rin to the right of the register state
    s += rin
    return s

# Example usage
register_state = "11010"
register_input = "1"
updated_state = shift(register_state, register_input)
print(f"Updated register state: {updated_state}")
