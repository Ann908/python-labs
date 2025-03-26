import hashlib
my_dict = {'login': 'alice_to', 'my_password': hashlib.md5('userpassword'.encode()).hexdigest(),
           'pib': 'Alice Ivanivna Savastru'}

password = input("Input your password: ")
def correct_password(password):

    hashed_pass = hashlib.md5(password.encode()).hexdigest()

    if hashed_pass == my_dict['my_password']:
        print("Password is correct!")
    else:
        print("Password is wrong!")
        password_new = input("Please, input password again: ")
        hashed_new_password = hashlib.md5(password_new.encode()).hexdigest()
        if hashed_new_password == my_dict['my_password']:
            print("Password is correct!")
        else:
            print("You don't have any attempts!")

correct_password(password)





