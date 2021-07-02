import register
import dashboard
import main 
import csv

def main():
    print '-----------------------------'
    print 'Login'
    print '-----------------------------'    
    username = input('Username: ')
    password = input('Pssword: ')
    new = user(username, password)
    if new.check_user() == True:
        if new.log() == True:
            print 'Successfully logged in'
            dashboard.main()
        else:
            print 'Username and password are not match'
            check = input("Do you want to try again: ")
            if check == 'yes' or 'Yes':
                main()
            else:
                main.main()
    else:
        print 'Username not exist'
        test = input('Do you want to register:')
        if test == 'yes' or 'Yes':
            register.main()
        else:
            main.main()
    
    

if __name__ == "__main__":
    main()