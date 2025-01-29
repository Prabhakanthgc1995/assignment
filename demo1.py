my_list = [10, 30, 45, "kanth" , 84 , 52, "prabha" ]

my_dict = {
            "name":"prabhakanth",
            "age": 29,
            "city": "mandya"
            }

my_list1 = []
if "kanth" in my_list:
    print("Element Found")
else:
    print("Element not Found")


if my_list1:
    print("List contains Values")
else:
    print("Empty!!")

print("\n")

if "name" in my_dict:
    print("Key Found")
else:
    print("Key Not Found")
print("\n")

if "name" in my_dict.values():
    print("Value Found")
else:
    print("Value Not Found")

print("\n")
if my_dict["name"] == "prabhakanth":
    print("Key contains the value")
else:
    print("Key Not found")

found = True

if not found:
    print("True")
else:
    print("False")

print("\n")

if my_dict:
    print("Dictionary is not empty")
else:
    print("Dict is empty")
