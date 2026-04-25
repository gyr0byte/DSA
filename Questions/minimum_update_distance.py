def min_steps(str1, str2, i1 = 0, i2 = 0):
    if i1 == len(str1):
        return len(str2) - i2
    elif i2 == len(str2):
        return len(str1) - i1
    elif str1[i1] == str2[i2]:
        return min_steps(str1, str2, i1 + 1, i2 + 1)
    

str1 = "intention"
str2 = "execution"
