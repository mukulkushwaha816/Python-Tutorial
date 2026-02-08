#ask user to print a number containing more than one digit and calculate then print???


number = input ("enter  a number")
total = 0
i = 0
while i< len (number):
    total += int(number[i])
i+=1
print (total)