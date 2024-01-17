#to strings in variables and  my_str is the variable name
my_str = "hello world"
print (my_str)

#to add items to a list
my_list = ["orange", "mango", "apple"]
my_list.append("banana")
print(my_list)

#to sort function
alpha_list = [43,84,43,23,59,3]
alpha_list.sort()
print(alpha_list)

#while loops in python
#print as long as x is less than 6
i = 1
while i<6:
    print(1)
    i +=1

#to create a python dictionary
new_dict = {
    "brand": "Honda",
    "model":"civic",
    "year":2005
}
print(new_dict)

#change the "year" to 2010
new_dict = {
    "brand": "Honda",
    "model":"civic",
    "year":2005
}
new_dict["year"] = 2010
print(new_dict)

#to create a tuple
my_tuple = (1,2,3,4,5)
print(my_tuple)

#to convert dictionary into a list of tuples
my_dictionary = {'a':1,'b':2,'c':3}
my_view = my_dictionary.items()
my_list = list(my_view)
print(my_list)

#fetch a specific element with indexing in tuples
my_tuple = ("mango","orange","apple")
print(my_tuple)

print(my_tuple[1])

#Build in functions in python
#Input() prompts the user for some input
name = input("Hi! what's your name: ")
print("Nice to meet you" " " + name + "!")
age = input("How old are you: ")
print("So, you are already"  " " + str(age) + "years old," + name + "!")


#if else with user input
age = int(input("Enter you age:"))

if age >= 18:
    print("eligible to vote")
elif age < 0:
    print("invalid input")
else:
    print("not eligible to vote")

#if else statement
age = 10
    
if age < 5:
    print("tecket price is 0")
elif age < 18:
    print("ticket price is 20")
else:
    print("ticket price is 20")

#functions in python
def add_numbers(x,y,z):
    a = x + y
    b = x + z
    c = y + z
    print(a,b,c)

add_numbers(1,2,3)

#function to display your name
def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("clive", "ouma")

print(full_name)

#function to display your birthday
def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print("Happy birthday to you!")

happy_birthday("clive",20)

#function to give invoice
def display_invoice(username, amount,due_date):
    print(f"Hello {username}")
    print(f"Your bill of ksh {amount} is due: {due_date}")

display_invoice("clive", 200, "10/02/2024")

#troubleshooting errors in python
my_dictionary = {'a':1,'b':2,'c':3}
try:
    value = my_dictionary["d"]
except KeyError:
    print("The key does not exist") 

#try/except with else to confirm errors in python
my_dictionary = {'a':1,'b':2,'c':3}

try:
    value = my_dictionary["b"]
except KeyError:
    print("A keyError occured")
else:
    print("No error occured")

#python classes and objects
class Student:
    def check_pass_fail(self):
        if self.marks >= 50:
            return True
        else:
            return False

Student1 = Student()
Student1.name = "clive"
Student1.marks = 80

have_pass = Student1.check_pass_fail()
print(have_pass)

Student2 = Student()
Student2.name = "kamau"
Student2.marks = 20

have_pass = Student2.check_pass_fail()
print(have_pass)

#init method
#it automatically gets called everytime objects are created
class Student:
    def check_pass_fail(self):
        if self.marks >= 50:
            return True
        else:
            return False
    #initialize the attributes   
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

student1 = Student("clive", 80)
student2 = Student("kamau", 30)
have_pass = student1.check_pass_fail()
print(have_pass)
have_pass = student2.check_pass_fail()
print(have_pass)

    

