#create a number guessing game
#make a variable,like winning_number and assign any number to it
#ask user to guess a number
#if user guessed correctly then print "YOU WIN !!!"
#if user guessed lower then actual number then print"too low"
#if user guessed higher than actual number the print"too high"




winning_number = 27
user_input = input("guess a number b/w 1 too 100:")
user_input = int(user_input)
if user_input == winning_number:
    print("YOU WIN !!!")
else:
    if user_input< winning_number:
        print ("too low")
    else:
        print("too high")
        
