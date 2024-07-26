#01 - Another function is 
def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="World"):   #def hello(to="saad"):
    print('Hello,', to.strip().title())
    
main()

#02 - Another function is 

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))
    
def square(n):
    return n * n
    #other two ways to get exponent are 
    return n**2
    return pow(n,2)

main()

