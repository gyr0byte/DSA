def lcs_recursive(seq1, seq2, idx1 = 0, idx2 = 0):
    if idx1 == len(seq1) or idx2 == len(seq2):
        return 0
    
    elif seq1[idx1] == seq2[idx2]:
        return 1 + lcs_recursive(seq1, seq2, idx1 + 1, idx2 + 1)
    
    else:
        option1 = lcs_recursive(seq1, seq2, idx1 + 1, idx2)
        option2 = lcs_recursive(seq1, seq2, idx1, idx2 + 1)
        return max(option1, option2)
    
print(lcs_recursive("analogy", "alchemy"))
print(lcs_recursive("AGGTAB", "GXTXAYB"))
print(lcs_recursive("ABCDGH", "AEDFHR"))
print(lcs_recursive("AAAA", "AA"))
print(lcs_recursive("AGGTAB", "AGGTAB"))
print(lcs_recursive("AGGTAB", "AGGTABX"))
print(lcs_recursive("intention", "execution"))