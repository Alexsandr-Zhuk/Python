#Specific_power

kg = input("Car_weight: ")
ls = input("Engine_power: ")
result = []

def power(x, y):
    p = x / y
    return p


result.append(power(int(kg), int(ls)))

print(f"Specific_power: {result}")
