# Specific_power
def power(x,y):
    p = x/y
    return p

x = int(input("Car_weight,kg: "))
y = int(input("Engine_power,ls.: "))
result = []

result.append(power(int(x), int(y)))

print(f"Specific_power: {result}")
