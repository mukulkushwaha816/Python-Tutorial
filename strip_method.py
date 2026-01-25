#name = "     mukul    "
#dots = ".............."
#print(name + dots)
#print(name.lstrip()+dots)
#print(name.rstrip()+dots)
#print(name.strip()+dots)
#print(name.replace(" ", "")+dots)
#print(name.replace(" ", ""))



name, char = input("enter comma seprated name and character : ").split(",")
print(f"length of your name is{len(name)}")
print(f"character count : {name.lower().count(char.lower())}")