<<<<<<< HEAD
# dic = {
#     "1": "a",
#     "2": "b",
#     "3": "c",
#     "4": "d"
# }

# print(dic["1"])
# print(dic.get["5"])
for i in range(1,1111111):
    print(i)
=======
import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First game")

x = 50
y = 50
width = 40
height = 60
vel = 5

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
>>>>>>> faa9f56a611c8cca2259cabbe68da46a1776f127
