# Part one
x = 31
print("Decimal and Binary/Hex representation:")
print(x, "in binary is", bin(x), "and in hexadecimal is", hex(x))
# part 2, identifying the error
x = 1.825
# error object not interpreted as integer
# correcting error
x = 18
print("\nCorrected value of x:, x")
# part 3 assigning binary or hex value
y = 0b1011  # represents 11 in binary
z = 0xA3    # hexadecimal of 163
print("\nBinary and Hex assigned to variables:")
print("y =", y, "z =", z)
# part 4 adding numbers
w = x + y + z
print("\nSum of x, y, z in decimal:")
print("The sum is", w)
# compression calculation
original_size = 240
compressed_text_size = 148
dictionary_size = 25
# calculate total compressed size
total_compressed = compressed_text_size + dictionary_size
compression_percent = (1 - (total_compressed / original_size)) * 100
# print results with formatted output
print("\nCompression Results")
print(" Compressed text size:", compressed_text_size, "characters")
print(" Dictionary size:", dictionary_size, "characters")
print(" Total:", total_compressed, "characters")
print(" Original text size:", original_size, "characters")
print(" Compression: {:.2f}%.".format(compression_percent))
# extra credit attempt
def twos_complement(decimal_num):
    if decimal_num < -128 or decimal_num > 127:
        return "Error: Number out of range"
    if decimal_num >= 0:
        return format(decimal_num, '#08b')
    # test with user input
    num = int(input("\nEnter a decimal number (-128 to 127) for two's complement: "))
    print("Two's complement (8-bit) of", num, "is", twos_complement(num))

