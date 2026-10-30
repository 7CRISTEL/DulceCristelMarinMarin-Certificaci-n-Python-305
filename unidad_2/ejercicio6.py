matriz=[
    ["A","B","C","D","E"],
    ["F","G","H","I","J"],
    ["K","L","M","N","Ñ"],
    ["O","P","Q","R","S"],
    ["T","U","V","W","X"],
    ["Y","X"," "," "," "]
]

for i in range(6):
    for j in range(5):
        print(f"posicion[{i}][{j}]={matriz[i][j]}")