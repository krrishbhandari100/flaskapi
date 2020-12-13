# num = int(input("Enter a number"))

def func(n):
    if(n==""):
        print("blank not allowed")
    else:
        n = int(n)
        # Changed num variable to string, 
        # and calculated the length (number of digits)
        order = len(str(n))

        # initialize sum
        sum = 0

        # find the sum of the cube of each digit
        temp = n
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10

        # display the result
        if n == sum:
            return True
        else:
            return False