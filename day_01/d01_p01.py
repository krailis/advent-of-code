import math

with open('d01.txt') as f:
    content = f.read()
module_masses = map(int, list(content.strip().split()))
module_fuel_req = [math.floor(x / 3) - 2 for x in module_masses]
print(sum(module_fuel_req))
