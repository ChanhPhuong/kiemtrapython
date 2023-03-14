import random

def generate_input_file(filename, num_shapes):
    shapes = ["#Rect", "#Circle", "#Triangle"]
    with open(filename,"w" ) as file:
        for i in range(num_shapes):
            shape = random.choice(shapes)
            file.write(shape + "\n")
            if shape == "#Rect":
                width = random.randint(1, 10)
                height = random.randint(1, 10)
                x = random.randint(-10, 10)
                y = random.randint(-10, 10)
                file.write(str(width) + " " + str(height) + "\n")
                file.write(str(x) + " " + str(y) + "\n")
            elif shape == "#Circle":
                radius = random.randint(1, 10)
                x = random.randint(-10, 10)
                y = random.randint(-10, 10)
                file.write(str(radius) + "\n")
                file.write(str(x) + " " + str(y) + "\n")
            elif shape == "#Triangle":
                a = random.randint(1, 10)
                b = random.randint(1, 10)
                c = random.randint(1, 10)
                x = random.randint(-10, 10)
                y = random.randint(-10, 10)
                file.write(str(a) + " " + str(b) + " " + str(c) + "\n")
                file.write(str(x) + " " + str(y) + "\n")

generate_input_file("input.txt",10)