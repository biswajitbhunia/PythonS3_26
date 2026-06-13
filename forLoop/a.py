# program to find the sum of the first n natural numbers
def sum_of_natural_numbers(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum
# take input from the user
n = int(input("Enter a positive integer: "))
result = sum_of_natural_numbers(n)
print("The sum of the first", n, "natural numbers is:", result)