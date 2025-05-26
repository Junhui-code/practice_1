part_val = 0x00

print("On what digit, u want 1 appear?")
digit = int(input())

value = pow(2, digit)
part_val = part_val |value

print("The result value is", bin(part_val))
print("\nSee? 1 appear on", "digit", digit)