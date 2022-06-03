userpin = input("ENTER YOUR PIN:")
def verify_pin(pin):
    if pin == userpin:
        return True
    else:
        return False

def log_in():
    print("NOTE:If you have three consecutive failures, the police will be called. ")
    tries = 0
    while tries < 3:
        pin = input('ENTER YOUR PIN:')
        if verify_pin(pin):
            print("The pin you entered is valid.")

            return True
        else:
            print("The pin you entered is invalid.")
            tries += 1
    print("Too many failed attempts. I'm calling the cops. Turning off the login button")
    return False

def start_menu():
    print("Welcome to the atm!")
    if log_in():
        print("You have successfully logged in!")
start_menu()