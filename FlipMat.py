m,n=map(int,input("No. of rows and columns (Seperate with space):").split())
mat = []
for r in range(m):
        mat.append(input("Enter element of the row:").split())
        mat[r]=list(map(int,mat[r]))
print(mat)
while True:   
    option=input("Enter 'h' for horizontal flip or 'v' for vertical flip and e for EXIT: ")
    if option=='e':
        break
    if option=='h'or option=='H':
        for r in mat:
            print((r[::-1]))
        

    elif option=='v'or option=='V':
        print(mat[::-1])