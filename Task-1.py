# 1)Create a class called Add, it must have _call_ defined. Create an object of that class. When the object is directly called with a list of integers -like- obj([1,2,3,4,5]) It must return the sum of elements in the list.
# eg:
# add = Add()
# total = add ([1,2,3,4,5,6])


class Add:
    def __call__(self, numbers):
        if isinstance(numbers, list) and all(isinstance(num, int) for num in numbers):
            return sum(numbers)
        else:
            raise ValueError("Invalid input. Please provide a list of integers.")

add_object = Add()

total = add_object([10,11,12,13,14])

print("Total sum:", total)

