def multiplication_table(n, m):
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            print(i * j, end=' ')
        print()


n = int(input('Enter the first number: : '))
m = int(input('Enter the second number: : '))
print("Multiplication Table of", n, "X", m, "=")
multiplication_table(n, m)
