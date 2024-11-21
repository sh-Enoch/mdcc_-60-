#!/ucr/bin/env python3
"""Program declares 2 ints and perform basic arithmetic."""

def arith(a, b):
    """Perform basic arithemetic on a, b."""
    sum = a + b
    print("The sum of {} and {} is {}".format(a, b, sum))

    diff = a - b 
    print("The difference between {} and {} is {}".format(a, b, diff))

    if a == 0 or b == 0:
        print("Sorry you will get an error")
    else:
        div =  a/b
        print("{} / {} = {}".format(a, b, div))



arith(9, 3)
arith(0, 5)
arith(10, 0)
arith(2334, 22)
