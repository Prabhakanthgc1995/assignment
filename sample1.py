my_list=[28, 38, 68, 9, 76, 56, 98, 45, 11]
total=sum(my_list)
print("The elemrnts in the list are:", my_list)
print("The sum of elements is:", total)
print("\n")
my_list.sort()
print("The elements in ascending order are:", my_list)
print("\n")
my_list.sort(reverse=True)
print("The elements in descending order are:", my_list)
print("\n")
even_number=[num for num in my_list if num % 2 == 0]
print("The even numbers are:" , even_number)
