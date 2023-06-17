import dbHandler
import cryptoFunctions
import getpass

if __name__ == '__main__':
    print("Welcome to the login system.")
    print("Do you wish to login (1) or create new user (2)?")
    choice = int(input("Enter choice: "))

    if choice == 1:
        while True:
            username = input("Enter username: ")
            passentry = getpass.getpass("Enter password: ")
            
            try:
                data = dbHandler.retrieve_user(username)

            except:
                print("Error - username or password incorrect.")
                continue

            hashed_password = data[2]
            salt = data[3]
            hash_attempt = cryptoFunctions.hash_password(passentry, salt)
            
            if hash_attempt != hashed_password:
                print("Error - username or password incorrect.")
                continue

            else:
                break

        print("Password correct!")


    if choice == 2:
        while True:
            username = input("Enter username: ")
            
            if dbHandler.check_duplicate_user(username):
                continue
            
            passentry = getpass.getpass("Enter password: ")
            passentry2 = getpass.getpass("Reenter password: ")

            if passentry == passentry2:
                break

            else:
                print("Passwords do not match!")
                continue

        salt = cryptoFunctions.create_salt()
        hashed_password = cryptoFunctions.hash_password(passentry, salt)
        dbHandler.create_user(username, hashed_password, salt)
