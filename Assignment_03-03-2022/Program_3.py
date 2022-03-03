# Write A program to print all the prime number between 2 and 500
num = 2
isPrime = True
print("Prime number between 2 and 500 -")
while num < 500:
    for i in range(2, num):
        if num % i == 0:
            isPrime = False
            break
    if isPrime:
        print(num)
    isPrime = True
    num = num+1





