# solution using recursion
def min_steps(str1, str2, i1 = 0, i2 = 0):
    if i1 == len(str1):
        return len(str2) - i2
    elif i2 == len(str2):
        return len(str1) - i1
    elif str1[i1] == str2[i2]:
        return min_steps(str1, str2, i1 + 1, i2 + 1)
    else:
        return 1 + min(min_steps(str1, str2, i1 + 1, i2), # deletion
                       min_steps(str1, str2, i1 + 1, i2 + 1), # swap
                       min_steps(str1, str2, i1, i2 + 1)) # insertion

# solution using memoization
def min_steps_memo(str1, str2):
    memo = {}
    def recurse(i1, i2):
        key = i1, i2
        if key in memo:
            return memo[key]
        elif i1 == len(str1):
            memo[key] = len(str2) - i2
        elif i2 == len(str2):
            memo[key] = len(str1) - i1
        elif str1[i1] == str2[i2]:
            memo[key] = recurse(i1+1, i2+1)
        else:
            memo[key] = 1 + min(recurse(i1 + 1, i2), # deletion
                                recurse(i1 + 1, i2 + 1), # swap
                                recurse(i1, i2 + 1))  # insertion 
str1 = "intention"
str2 = "execution"
print(min_steps(str1, str2))