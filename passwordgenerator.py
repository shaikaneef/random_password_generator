import string
import random
def Password_Generator():

    lower_case=string.ascii_lowercase # all the charecters from a-z
    
    upper_case=string.ascii_uppercase # all the charecters from A-Z

    numbers=string.digits # integer values from 0-9

    special_charecters=string.punctuation  # all the special charecters 

    
    password=[]
    password.extend(list(lower_case))
    password.extend(list(upper_case))
    password.extend(list(numbers))
    password.extend(list(special_charecters))
    random.shuffle(password)
  
    print("Your password is : ")
    print("".join(random.sample(password,password_length)))


try:
    password_length=int(input("Enter password length: "))
except:
    password_length=int(input("Please Enter an integer value : "))
finally:
    Password_Generator()

        

    

    



