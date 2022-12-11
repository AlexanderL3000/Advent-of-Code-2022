with open("02Input.txt") as f:
    data = f.read()
f.close()

data = data.splitlines()

score = 0
for item in data:
    # Rock
    if item[0] == "A":
        if item[2] == "X":
            score += 3
        elif item[2] == "Y":
            score += 4
        elif item[2] == "Z":
            score += 8
    elif item[0] == "B":
        if item[2] == "X":
            score += 1
        elif item[2] == "Y":
            score += 5
        elif item[2] == "Z":
            score += 9

    elif item[0] == "C":
        if item[2] == "X":
            score += 2
        elif item[2] == "Y":
            score += 6
        elif item[2] == "Z":
            score += 7

print(score)