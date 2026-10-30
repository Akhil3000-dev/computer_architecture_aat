# Computer Architecture Assignment - Problem Solving Group 1
# QUESTION 1 
def to_binary(num, bits):
    # for negative numbers
    if num < 0:
        num = num + 2 ** bits
    return format(num, "0" + str(bits) + "b")

def to_decimal(binary):
    value = int(binary, 2)
    if binary[0] == "1":          
        value = value - 2 ** len(binary)
    return value

def add(a, b):
    print("Expression:", a, "+", b)
    print("Operand 1 (8-bit):", to_binary(a, 8))
    print("Operand 2 (8-bit):", to_binary(b, 8))
    # addition in 16-bit
    total = a + b
    if total < -32768 or total > 32767:
        print("Overflow occurred")
    else:
        print("No overflow")
    result = to_binary(total, 16)

    print("Result in binary :", result)
    print("Result in decimal:", to_decimal(result))
    print()

print("QUESTION 1")
print("a)")
add(24, 17)
print("b)")
add(-25, -18)


