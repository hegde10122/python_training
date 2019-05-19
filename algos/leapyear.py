'''
Write a function checkLeapYear with an integer parameter named year.

The parameter needs to be greater than one and less than or equal to 9999.

If the parameter is not in the range return "out of range error".

Otherwise,if it is in valid range, calculate if it is a leap year and return message "Leap year" if it is a leap year or else return "Not a leap year".

A year will be a leap year if it is divisible by 4 but not by 100. 
If a year is divisible by 4 and by 100, it is not a leap year unless it is also divisible by 400.

'''

'''
The algorithm development is very straightforward.

First we need to ensure that the user is allowed to enter a natural number in the range 1 - 9999.

A leap year is that year which is divisible by 4 (meaning the remainder produced is 0) but not divisible by 100.
A leap year is also that year that is divisible by 400. When we consider a number that is divisible by 400, we realise that it is 
not required for us to check it's divisibility both by 4 and 100. 
A number that is divisible by 400 is implicitly divisible by both 4 and 100. Check that this case is true for numbers like 
800,1200,1600 and 2400.

Using the ideas above we write the pseudocode.

algorithm checkLeapYear(year<natural number>)
This algorithm reads an input natural number as year and prints whether it is leap year or not.
    Pre year must in the range 1 to 9999 (both inclusive)
    Post Print whether the number entered is leap year or not
    Return true if the number is leap year or else return false
1   remainder = year mod 400  //where mod indicates remainder after division
2   if (remainder equal 0)
    1  print("Leap year")
    2  return true
3   else
    1  if( (year mod 4 equal 0) AND (year mod 100 not equal 0) )
       1 print("Leap year")
       2 return true
    2  else
       1  print("Not a leap year")
       2  return false
    3  end if   
4   end if    
end checkLeapYear
'''


def checkLeapYear(year):
    #step 1: check year to be of type integer or else flash input error to the user
    if(not isinstance(year,int)):
        print("Input must be an integer")
    elif year < 1 or year > 9999:
        print("Input must be an integer in range (1-9999).Out of range error")
    else:
        if ((year % 4 == 0 and year % 100 !=0) or (year % 400 == 0)):
            print(year,"is a leap year")
        else:
            print(year,"is not a leap year")

checkLeapYear(21212)
checkLeapYear(2000)
checkLeapYear(1988)
checkLeapYear(2020)
checkLeapYear(1)
checkLeapYear(1700)
checkLeapYear(1900)
checkLeapYear(1840)
checkLeapYear(1999)
checkLeapYear(-123)
checkLeapYear("year")
checkLeapYear(2092)
