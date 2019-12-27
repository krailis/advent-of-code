import math

with open('d01.txt') as f:
    content = f.read()
module_masses = map(int, list(content.strip().split()))

total_fuel_req = 0
while True:
    module_fuel_req = [math.floor(x / 3) - 2 for x in module_masses]
    module_masses = [x for x in module_fuel_req if x > 0]
    if len(module_masses) == 0:
        break
    total_fuel_req += sum(module_masses)
print(total_fuel_req)
