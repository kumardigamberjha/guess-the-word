import random
# list to be selected

l1= ["apple", 'banana', "mango", "cherry", "guava"]
# select randomly
choice= random.choice(l1)
print(choice)

print("Select any of the given option:- ", l1)


chance= 5

for i in range(chance):
    user= input()
    if user== choice:
        print("User wins with", chance-1,"moves left")
        break

    elif user not in l1:
        print("Invalid choice", chance,"moves left")

    else:
        print("You made an incorrect choice! Please choose again", chance,"moves left")

    chance-=1