from random import randint
def Create_map(size):
    Global_map = []
    for i in range(size):
        check = []
        for i in range(size):
            check.append(10)
        Global_map.append(check)
    print(Global_map)
    for i in range(1, size):
        for j in range(1, size):
            a = Global_map[i][j-1]
            b = Global_map[i-1][j] 
            c = Global_map[i-1][j-1]
            Global_map[i][j] = int((a + b + c)/3) + randint(-1, 1)

    with open("Map.txt", "w") as file:
        
        for i in range(size):
            line = ""
            for j in range(size):
                line += str(Global_map[i][j]) + " "
            file.write(line + "\n")
Create_map(10)