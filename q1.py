def longest_palindromic_substring(s):
    a=len(s)
    c=""
    for i in range(a):
        for b in range(i,a):
            n=s[i:(b+1)]
            if n==n[::-1]:
                if len(n)>len(c) and len(n)>1:
                    c=n
    return c
                    
            