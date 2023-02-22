def to_gctu(file_name):

    # Define the input string
    input_string = '''
30000000 10A0A624
10000000 50000000
31000000 0000009C
30100000 00000000
10000000 50000000
31000000 0000070C
06120000 00000000
01000101 00000000
00120000 01000101
D0000000 DEADCAFE
    '''
    
    # Conver the input string be a straight string like "3000000010A0A624D0000000DEADCAFE"
    input_str = input_string.replace(" ", "").replace("\n", "")
    output_str = ""
    for i in range(0, len(input_string), 17):
        output_str += input_string[i:i+17]

    # Convert the forammted string to binary data
    binary_data = bytes.fromhex(output_str)

    # Write the binary data to a file
    with open(file_name, 'wb') as f:
        f.write(binary_data)

def from_gctu(file_name):

    # Open the .gctu file
    with open(file_name,'rb') as f:
        output_string = f.read()
        f.close()

    # Read the file as upper-case Hex
    output_string = output_string.hex().upper()

    # Format the .gctu Contents into proper Code format
    new_output_string = ""
    for i in range(0, len(output_string), 16):
        new_output_string += output_string[i:i+8] + " " + output_string[i+8:i+16] + "\n"

    # Print the output string without an extra line break at the end
    print(new_output_string, end="")
    
if __name__ == "__main__":
    to_gctu("test.gctu")
    from_gctu("test.gctu")
