def remove_adjacent_duplicates(s):
    prime=False
    while not prime:
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                prime=False
                s=s[:i]+s[i+2:]
                break
            else:
                prime=True
    return s
            
                
                
                
            
        