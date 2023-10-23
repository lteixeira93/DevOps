import math

def circ(raio: float) -> float:
    return 2 * math.pi * raio

print(circ.__annotations__) # Verify funtion in depth
    