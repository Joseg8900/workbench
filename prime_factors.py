def solution(num):
    prime_factors = []
    for i in range(2,int(num**.5)+1):
        if(num%i==0):
            #Base case for 2 or perfect squares (9,25)
            if(i==2 or i*i==num):
                prime_factors.append(i)

            #Numbers that are factors of num but not even.
            elif(i%2!=0):
                if(len(solution(i))==0):
                    prime_factors.append(i)

            #Numbers larger than the sqrt(num) that are factors of num
            elif(num%int(num/i)==0 and int(num/i)%2!=0):
                if(len(solution(num/i))==0):
                    prime_factors.append(i)

    return prime_factors

def prime_factors(n):
    factors = []
    # Handle the case for 2
    if n%2 == 0:
        factors.append(2)
    while n%2==0:
        n //=2

    # Check for odd factors from 3 up to the square root of n
    for i in range(3, int(n**.5)+1, 2):
        while n % i == 0:
            if i not in factors:
                factors.append(i)
            n //= i
    
    # If n is still greater than 2, it means it's a prime number itself
    if n > 2:
        factors.append(n)
    return factors

print(prime_factors(45))