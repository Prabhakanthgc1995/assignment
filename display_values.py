class example:
    def __init__(self, str1, str2):  # Corrected __init__ method name
        self.name1 = str1
        self.name2 = str2
        self.name3 = "Devops"

    def print_value(self):
        print(self.name1, self.name2, self.name3)

    def display_value(self, str2):
        print(str2)

# Creating instances of the example class
var = example("Hello", "Welcome")
var.print_value()        # This will print: Hello Welcome Devops
var.display_value("Training")  # This will print: Training

var1 = example("Prabha", "kanth")
var1.print_value()       # This will print: Prabha kanth Devops
var.print_value()        # This will print: Hello Welcome Devops

