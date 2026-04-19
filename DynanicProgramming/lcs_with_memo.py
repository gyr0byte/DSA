def lcs_memo(seq1, seq2):
    memo = {}
    def recurse(idx1 = 0, idx2 = 0):
        key = (idx1, idx2)
        if key in memo:
            return memo[key]
        
        elif idx1 == len(seq1) or idx2 == len(seq2):
            memo[key] = 0
        
        elif seq1[idx1] == seq2[idx2]:
            memo[key] = 1 + recurse(idx1 + 1, idx2 + 1)
        