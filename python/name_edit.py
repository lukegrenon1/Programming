def count_name():
    loop = True
    while loop:
        count = 0
        user = input('Enter your name, "q" to quit: ').lower()
        while user == '':
            user = input('Please enter your name, "q" to quit: ').lower()
        if (user != 'q'):
            char = input('Enter the letter you would like to count: ').lower()
            while char == '':
                char = input('Please enter the letter you would like to count: ').lower()
            for l in user:
                if l == char:
                    count += 1
            print('There is ' + str(count) + ' ' + char + ' in ' + user)

            # select character to delete from name
            delete = input('What letter from ' + user + ' would you like to remove? ').lower()
            for l in user:
                if l == delete:
                    name_edit = user.split(delete)
                    name = ' '.join(name_edit)
                    print(name)
                    break
                elif l != delete:
                    delete = input('You did not choose a letter. What letter from ' + user + ' would you like to remove? ').lower()
        else:
            print('Program Terminated')
            loop = False
            
def main():
    count_name()
    loop = True
    

main()
