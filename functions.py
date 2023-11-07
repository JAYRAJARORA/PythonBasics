def my_func(n, m):
    return m * n


print(my_func(3, 4))


def outer(a, b):
    c = "c"

    def inner():
        return a + b + c

    return inner()


print(outer("a", "b"))


def double(arr, val):
    def helper():
        for index, value in enumerate(arr):
            arr[index] *= 2

        # modifying the val works only in this function
        # val = 5
        # to modify it outside use nonlocal
        nonlocal val
        val = 5
    helper()
    print(arr, val)
    return


double([1, 2, 4, 3], 10)
