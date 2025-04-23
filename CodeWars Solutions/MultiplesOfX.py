# Create a function with two arguments that will return an array of the first n multiples of x.
# Note: this is the first solution with list comprehension!

def count_by(x, n):
    return [x*i for i in range(1,n+1)]
