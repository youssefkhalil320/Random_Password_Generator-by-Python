import string
import random             #responsible for randmoing the elements 

#creating the lists which contain uppercase and lowercase letters, digits and punctuation. 
group1 = list(string.ascii_uppercase)
group2 = list(string.ascii_lowercase)
group3 = list(string.digits)
group4 = list(string.punctuation)

#printing welcome Message and taking the input 
print("Welcome to HekyBeky password generator")
print("Please enter a number greater than or equal 6")
wanted_number = input("Enter the Number Here:  ")

#checking if the input is valid 
while True:
    try:
        number = int(wanted_number)
        if number < 6:
            print("Please enter a number greater than or equal 6")
            wanted_number = input("Enter the Number Here:  ")
        else:
            break

    except:
        print("Please, Enter an Integer")
        wanted_number = input("Enter the Number Here:  ")  
#shuffling the elemenys groups 
random.shuffle(group1)
random.shuffle(group2)
random.shuffle(group3)
random.shuffle(group4)       

#calculating the precentage of each group 
first_part  = round(number * (30/100))
second_part = round(number * (20/100))

#generating the password 
password = []
for i in range(first_part):
    password.append(group1[i])
    password.append(group2[i])

for i in range(first_part):
    password.append(group3[i])
    password.append(group4[i])    

random.shuffle(password)             #shuffling the password again to be satisfy 
Real_password = "".join(password)    # join the charecters in the list to form the password 
print(Real_password)                 # printing the password 
