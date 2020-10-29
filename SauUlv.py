# output looks better if we pause a bit in each iteration
from time import sleep

# parameters
A = 2/3
B = 1/15
C = 1/1
D = 1/400

def timestep(x, y, dt):
    """Run one timestep of the wolf-sheep system"""
    x += (A*x - B*x*y) * dt
    y += (D*x*y - C*y) * dt
    return x, y

# starting values
sheep = 400
wolf = 20
# time step size
dt = 0.2

# use _ when we don't need the loop variable later
for _ in range(500):
    # print a . for every 10 sheep
    print(f'{sheep:6.0f}', '.' * int(sheep/10))
    # print an x for every wolf
    print(f'{wolf:6.0f}', 'x' * int(wolf))
    # update the numbers
    sheep, wolf = timestep(sheep, wolf, dt)
    sleep(0.1) # pause for 0.1 seconds