while True:
    mylist = ['0', '', '']
    from random import shuffle


    def shuffle_list(mylist):
        shuffle(mylist)
        return mylist


    res = shuffle_list(mylist)

    def user_guess():
        guess = ''
        while guess not in ['0', '1', '2']:
            guess = input("enter a number from 0,1,2: ")
        return int(guess)


    number = user_guess()

    def check(res, number):
        if res[number] == '0':
            print("u won")
            print(res)

        else:
            print("u lost!")
            print(res)


    check(res, number)

    x = input("Do u want to play again? press '1' for yes else '0': ")
    if (x == '1'):
        continue
    else:
        break

