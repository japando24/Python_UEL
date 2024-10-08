from random import randrange
def guessNumber():
    while True: 
        somay = randrange(1, 101)
        solandoan = 0 
        win = False 
        while solandoan < 7: 
            solandoan += 1 
            songuoi = int(input("Enter to guess number [1-100]: "))
            print("The ", solandoan, "guess")
            if somay == songuoi: 
                print("Coongratulation!!!, You win. Result: ", somay)
                win = True 
                break 
            if somay > songuoi: 
                print("Wrong, number of pc is larger than your number")
            elif somay < songuoi:
                print("Wrong, number of pc is smaller than your number")
        if win == False: 
            print("GAME OVER !!! number of pc = ", somay)
        answer = input("Do you want to continue (y or n )")
        if answer == "n" or answer == "N": 
            break 
    print("Thank you for your join!!!")
if __name__ == "__main__":
    guessNumber()