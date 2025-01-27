
if 6 >= 3:
    print("hello world")

username =input("enter your name")
if username == "noname":
    print("welcome")

username =input("enter your name")
password =input("enter your name")
if username == "Noname" and password == "nopass":
    print("welcome")

else:
    print("wrong username eller password")

for i in range(32):
    print("hello world")

correct_password = "secret"
while user_password != correct_password:
    user_password = input("Enter the password: ")
print("Correct password!")


for i in range(5):
    number = int(input("Enter a number: "))
    if number > 5:
        print("högre än 5!")

while True:
    user_input = input("Enter a number: ")
    try:
        number = int(user_input)
        print("Thank you! You entered a valid number.")
        break
    except ValueError:
        print("That's not a valid number. Try again.")

