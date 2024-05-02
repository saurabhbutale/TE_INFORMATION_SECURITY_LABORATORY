def manipulate_string(input_string):
    result_and_binary = ""
    result_xor_binary = ""
    result_and_char = ""
    result_xor_char = ""

    for char in input_string:
        ascii_value = ord(char)
        binary_value = bin(ascii_value)[2:]
        manipulated_and = int(binary_value, 2) & 127
        manipulated_xor = int(binary_value, 2) ^ 127

        # Format binary results
        result_and_binary += f"{manipulated_and:08b} "
        result_xor_binary += f"{manipulated_xor:08b} "

        # Format character results
        result_and_char += chr(manipulated_and)
        result_xor_char += chr(manipulated_xor)

    return (result_and_binary, result_and_char), (result_xor_binary, result_xor_char)

input_string = "\\WadiaCoE Pune"  # Corrected the escape character
(result_and_binary, result_and_char), (result_xor_binary, result_xor_char) = manipulate_string(input_string)

print("Original String:", input_string, "\n")

print("AND Manipulation (Binary):", result_and_binary)
print("AND Manipulation (Character):", result_and_char, "\n")

print("XOR Manipulation (Binary):", result_xor_binary)
print("XOR Manipulation (Character):", result_xor_char, "\n")
