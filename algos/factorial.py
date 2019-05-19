'''
Given a number n, compute n factorial (written as n!) where n is greater than or equal to zero.

n! = 1x2x3x4x....x(n-1)xn for n>=1
0! = 1

Applying the factorial definition to the numbers after 0 we have,
    0! = 1
    1! = 1x1
    2! = 1x2
    3! = 1x2x3
    4! = 1x2x3x4
    and so on

    We observe that 4! contains all the factors of 3! multiplied by 4
    Thus we can generalise and say that 4! = 4 x 3!
    or n! = n x (n - 1)! for all n>=1
    
    Let us begin with a variable called product = 1
    This value 1 is nothing but 0!
    Thus we have product = 1 = 0! as the starting point. 
    
    product = 1 x 0! -------------- (1)
    
    Later on to compute 1! we can use the product in equation (1) above as
    product = 1 x product   ---- (2)

    For 2!, product = 2 x product (from equation 2)   ----(3)
    For 3!, product = 3 x product (from equation 3)   ----(4)
    and so on.

    For n! product = n x product from (n-1)! ----- (n)
    The equation (n) gives us an idea that we can use a loop to iteratively generate n!

    Thus the algorithm development can be wrapped up as follows:
    1) Treat 0! = 1 as the base case (product = 1)
    2) Build each of the n remainng product values using iteration over the predecessor values.
    3) Write the value of n factorial.

    Algorithm pseudocode

    algorithm factorial(number <integer>)
    This algorithm takes user integer as a parameter and returns its factorial value
       Pre number must be greater than or equal to zero
       Post Factorial printed.

    1  product = 1
    2  if (number < 0)
        1 print("Factorial undefined for negative integers)
        2 return -1
    3  else
       1 i = 2      
       2  loop (i <= number)
          1 product = product * i
          2 i = i + 1
       3  end loop
    4 return product
    end factorial           
'''


def factorial(number):
    if(not isinstance(number,int)):
        print("Input error.Integer expected")
        return -1
    elif number < 0:
        print("Input error.Negative integer not allowed")
        return -1
    else:
        product = 1
        i = 2
        while i <= number:
            product = product * i
            i = i + 1
        print("The factorial of ",number," is ",product)    
    return product

factorial(5)
factorial(-5)
factorial(0)
factorial(1)
factorial(50)
factorial(12)