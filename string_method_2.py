string = "she is beautiful and she is good dancer"
print (string.replace(" ","_"))
print (string.replace("is","was"))
print (string.find("is"))

is_pos1 = string.find("is")
is_pos2 = string.find("is",is_pos1+1)
print(is_pos2)