import register
import login
import main 
import csv

def main():
    print('-----------------------------')
    print('Dashboard')
    print('-----------------------------')
    check = input('Do you want to see all users:')
    if check == 'yes' or 'Yes':
        new.see_all()
    test = input('Do you want to change password:')
    if test == 'yes' or 'Yes':
        new_pass = input('new password: ')
        sec_pass = input('new password again: ')
        if new_pass == sec_pass:
            new.change_pass(new = new_pass)
        else:
            print 'Not match'
            main()
    ex = input('Do you want to exit:')
    if ex != 'yes' or 'Yes':
        main()

if __name__ == "__main__":
    main()