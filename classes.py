class MyClass:
    random_val = 12

    def __init__(self, nums):
        self.nums = nums
        self.size = len(nums)
        self.__private_var = 42

    def get_length(self):
        return self.size

    def get_double_length(self):
        return 2 * self.get_length()

    def get_squared_list(self):
        # adding a seed assigned to a private variable
        return [i**2 + self.__private_var for i in self.nums]

    @staticmethod
    def print_msg():
        print('This is a static method')


myObj = MyClass([1, 2, 3])
print(myObj.nums)
print(myObj.get_double_length())
print(myObj.get_squared_list())
# print(myObj.__private_var) - does not work since it is a private variable

# class method
MyClass.print_msg()
# class variable
print(MyClass.random_val)



