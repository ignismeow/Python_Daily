# Problem:1
# Given an integer, , perform the following conditional actions:
# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print('Weird')
    elif n % 2 == 0 and n >= 5:
        print('Not Weird')
    elif n % 2 == 0 and n >= 6:
        print('Weird')
    elif n % 2 == 0 and n > 20:
        print('Not Weird')

# Problem:2
#The provided code stub reads and integer, , from STDIN. For all non-negative integers , print i^2.
n = int(input())
  for i in range(n):
    print(i**2)
# Problem:3 Find leap year
def is_leap(year):
    leap = False
    # Write your logic here
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    else:
        leap = False
    return leap
year = int(input())
print(is_leap(year))
