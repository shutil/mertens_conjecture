import math
from matplotlib import pyplot as plt
#check weather the number is prime or not
def is_prime(num):
    number = num
    factors = []
    for x in range(1,number+1):
        if number % x == 0:
            factors.append(x)
    if len(factors) == 2:
        return "Prime"
    else:
        return "Not Prime"


#get out all the factors of that number
def factors(num):
    number = num
    prime_list = []
    num_list = []
    for x in range(1,number+1):
        if number % x == 0:
            num_list.append(x)
            check = is_prime(x)
            if check == "Prime":
                prime_list.append(x)
    return (prime_list,num_list)


def perfect_square(num):
    number = num

    ar = factors(number)[1]
    for x in ar:
        if x == 1:
            continue
        if x == math.pow(math.sqrt(x),2):
            return "Perfect square"
            break
    else:
        return "Not Perfect"


def points(num):
    number = num

    ar = factors(number)[1]
    for x in ar:
        ps = perfect_square(x)
        if ps == "Perfect square":
            return 0
            break
    else:
        n = len(factors(number)[0])
        if n%2 == 0:
            return 1
        else:
            return -1

x_axis = []
y_axis = []

for x in range(1,200):
    x_axis.append(x)
    y_axis.append(points(x))

print(x_axis)
print(y_axis)

plt.plot(x_axis,y_axis)
plt.show()