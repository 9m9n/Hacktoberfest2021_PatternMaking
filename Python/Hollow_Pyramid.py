n = int(input("Enter height of triangle: "))

for i in range(n):
    if (i == 0 or i == n-1):
        print('*'*(i+1))
    else:
        print('*' + ' '*(i-1) + '*')