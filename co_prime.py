
def solution(a,b):
    num:int = int(max(a,b)**.5)+1
    prime_a = set()
    prime_b = set()
    prime_x = set()
    
    for i in range(2,num):
        div_a = int(a/i)
        div_b = int(b/i)
        if(a%div_a==0 and b%div_b==0):
            prime_x.add(i)
        if(a%div_a==0):
            prime_a.add(div_a)
        if(b%div_b==0):
            prime_b.add(div_b)

    f_print(prime_a,a)
    f_print(prime_b,b)
    f_print(prime_x,num)
    print("##########")
    
    if(len(prime_x)==1):
        for x in prime_x:
            return (x in prime_a)^(x in prime_b)
    elif(len(prime_x)<1):
        for x in prime_x:
            
    else:
        return False


def f_print(nums,var):

    print(f"Prime_{var}: {len(nums)}")
    for num in nums:
        div = int(var/num)
        print(num,div)
    print("*****")


solution(4638, 4799) 
solution(5785, 9186) 
solution(2167, 2183)

print("False")
print(solution(22, 77))
print(solution(17, 51))