#slicing/selecting sub sequences
#lang = "python"
#syntax-[step argument]
#print ("mukul"[0:5:2])



#negative step argument
#print ("mukul"[-1::-1]) 



#Q.ask user name and print back user name in reverse order ?
name= input ("enter your name:")
reverse = name [-1::-1]
print (f"reverse of your name is {reverse}")