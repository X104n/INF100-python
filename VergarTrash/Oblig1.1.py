import math

def pi(d=2):
    if d <= 14:
        return round(math.pi, d)
    else:
        return "For mange desimaler"

print(pi(1))