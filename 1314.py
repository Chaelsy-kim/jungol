a=int(input())
num='A'
matrix = [[0 for col in range(a)] for row in range(a)]

for i in range(0,a):
    for j in range(0,a):
        if(i%2==0):
            matrix[j][i]=num
        else:
            matrix[a-j-1][i]=num
        if(num=='Z'):
            num='@'
        num=ord(num)
        num+=1
        num=chr(num)
        
for i in range(0,a):
    for j in range(0,a):
        print("%c" %matrix[i][j],end=' ')
    print(" ")