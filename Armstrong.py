def is_Armstong(n):
    temp=n
    sum=0
    #find the number of digits in the number
    num_digits=len(str(n))
    while temp>0:
        r=temp%10
        sum=sum+r**num_digits
        temp=temp//10
    if n==sum:
        return True
    else:
        return False

def is_armstrong(num):
    s = str(num)
    return num == sum(int(d) ** len(s) for d in s)

# Example usage: Print Armstrong numbers up to a range
n = int(input('Enter any range: '))
armstrong_numbers = [i for i in range(n) if is_armstrong(i)]
print(' '.join(map(str, armstrong_numbers)))

#n=int(input('Enter any Range :'))
#find the number of digits in the number
#for i in range(n):
#        if is_Armstong(i):
#            print(i,end=' ')
#