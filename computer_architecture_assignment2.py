#QUESTION 2
# Logical shift operations on 8-bit numbers

print("QUESTION 2")

# a) logical left shift by 2
num = "1111110110"[-8:]
print("a) Logical left shift by 2")
print("Original number:", num)
value = int(num, 2)
for i in range(1, 3):
    value = (value << 1) % 256        # keep only 8 bits
    print("After shift", i, ":", format(value, "08b"))
print("Final result:", format(value, "08b"))
print()

# b) logical right shift by 2
num = "10010100"
print("b) Logical right shift by 2")
print("Original number:", num)
value = int(num, 2)
for i in range(1, 3):
    value = value >> 1
    print("After shift", i, ":", format(value, "08b"))
print("Final result:", format(value, "08b"))
