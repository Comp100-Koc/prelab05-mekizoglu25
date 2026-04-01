def add_binary(a, b):
    def findint(x):
        x=x[2:]
        a=1
        sum=0
        x=x[::-1]
        for i in x:
            sum+=int(i)*a
            a=a*2
        return sum
    def findbin(x):
        string=""
        while not x==0:
            if x%2==0:
                x=x/2
                string="0"+string
            else:
                x=(x-1)/2
                string="1"+string
        return "0b"+string
    return findbin(findint(a)+findint(b))
            