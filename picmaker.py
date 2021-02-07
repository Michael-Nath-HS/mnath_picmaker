from random import randint
size = 500
f_name =  "image.ppm"
file = open(f_name, 'w')
file.write(f"P3 {size} {size} 255\n")
for i in range(size):
    for j in range(size):
        r = 255
        g = 255
        b = 255
        # preparing the rainbow fishscales
        if (((i * j) % 12) < 10):
            r = ((randint(1, 128) ** 2 - (i ** (j + 1)))) % 256
        if (((i * j) % 12) < 6):
            g = ((randint(1, 10) ** 2 - (i ** (j + 1)))) % 256
        if (((i * j) % 12) < 3):
            b = ((randint(1, 256) ** 2 - (i ** (j + 1)))) % 256
        # adding a shine to some of the scales
        if ((i + j) % 75 <= randint(0, 2)):
            if (j < randint(0, size // 2) and (i > randint(size//2, size)) or (j > randint(size//2, size)) and (i < randint(0, size // 2))):
                r = 255
                g = 255
                b = 0 + (i * j)
                
        file.write(f"{r} {g} {b} ")
    file.write('\n')
file.close()
print("IMAGE CREATED WITH NAME: image.png")