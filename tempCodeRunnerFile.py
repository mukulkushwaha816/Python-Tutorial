def comman_finder (l1,l2):
    output = []
    for i in l1:
        if i in l2:
            output.append(i)
            return output
print(comman_finder([1, 2, 5, 8][1, 2, 7, 6]))