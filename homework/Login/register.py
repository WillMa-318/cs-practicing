import dashboard
import login
import main 
import csv

def main():
    print ('-----------------------------')
    print ('Register')
    print ('-----------------------------')
    username = input('Username: ')
    password = input('Pssword: ')
    password_sec = input('password again: ')
    if password == password_sec:
        print ('Successfully Registered')
        new = user(username, password)
        new.push()
        check = input('Do you want to login:')
        if check == 'yes' or 'Yes':
            login.main()
        else:
            dashboard.main()
    else:
        print ('Password not match')
        main()

if __name__ == "__main__":
    main()