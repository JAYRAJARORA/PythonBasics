# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    n, m = 0, 'abc'
    print('n  = ', n)
    print('m = ', m)
    n += 1
    print(n)

    n = None
    print(type(n))
    print(n)

    n = input("Enter the number")
    n = int(n)
    if n <= 2:
        n -= 1
    elif 2 < n < 5:
        n += 1
    else:
        n += 2
    print(f'the value of n is {n}')

    n, m = 1, 2
    if ((n > 2 and
         n != m) or n == m):
        n += 1
    print(n)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
