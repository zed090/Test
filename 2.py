import math
with open("sonlar.txt","r") as file:
    with open("ildiz.txt","w") as file2:
        son = file.read().split()
        for i in son:
            ildiz=int(math.sqrt(int(i)))
            file2.write(f"{ildiz} ")
print("saved")                


