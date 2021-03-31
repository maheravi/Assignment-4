def checkered(a, b):
    for i in range(1, a + 1):
        if i % 2 == 0:
            for j in range(1, b + 1):
                if j % 2 == 0:
                    print('*', end='  ')
                else:
                    print('#', end='  ')
            print()
        else:
            for j in range(1, b + 1):
                if j % 2 == 0:
                    print('#', end='  ')
                else:
                    print('*', end='  ')
            print()


rows = int(input("Please Enter Number of Rows  : "))
columns = int(input("Please Enter Number of Columns  : "))
print("checkered Pattern")
checkered(rows, columns)

