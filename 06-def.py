def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="World"):   #def hello(to="saad"):
    print('Hello,', to.strip().title())
    
main()
