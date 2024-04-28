def calculate_in_bit(s, c, n):
    """
    Calculate the in_bit value using the given formula:
    in_bit = c1*s1 + c2*s2 + ... + cN*sN (mod 2)
    
    Args:
        s (list): List of s values (s1, s2, ..., sN)
        c (str): String representing the register cell clock values (e.g., "101010")
        n (int): Number of register cells (N)
    
    Returns:
        int: The calculated in_bit value
    """
    # Ensure that the length of c matches the number of register cells
    if len(c) != n:
        raise ValueError("Length of c must match the number of register cells (N)")

    # Initialize the in_bit value
    in_bit = 0

    # Calculate the in_bit using the formula
    for i in range(n):
        in_bit += int(c[i]) * s[i]

    # Take modulo 2
    in_bit %= 2

    return in_bit

# Example usage:
s_values = [1, 0, 1, 1]  # Example s values
clock_values = "1010"   # Example clock values
num_cells = len(s_values)

in_bit_result = calculate_in_bit(s_values, clock_values, num_cells)
print(f"The calculated in_bit value is: {in_bit_result}")
test_data = ()
('10001',50),
('1010111001111101',100),
('11001001011',500),
('110001010010101110010101010010100100101',1000)

    
