#Q1
while True:
    n = int(input("nhap_a:"))
    if n >= 5:
        break
    else:
        print("re_enter")
def calculate_S1(n):
    return sum(range(1, n + 1))
def calculate_S2(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
def calculate_S3(n):
    result = 0
    for i in range(1, n + 1):
        result += 1 / (i + 1)
    return result

s1 = calculate_S1(n)
s2 = calculate_S2(n)
s3 = calculate_S3(n)
print(s1,s2,s3)
import math
for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
       print(f"{n} is not a prime number")
       break
    else:
        print(f"{n} is a prime number")
#Q2
import math
def check_prime_number(num):
    if num<2:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num % i ==0:
            return False
    return True
def get_prime_divider(number):
    prime_dividers = []
    for i in range(2,number + 1):
        if check_prime_number(i) and number % i ==0:
            prime_dividers.append(i)
    return prime_dividers
def gcd(m,n):
    while n !=0:
        m, n = n, m%n
    return m
def lcm(m,n):
    return abs(m*n) // gcd(m,n)
m = int(input("enter_m:"))
n = int(input("enter_n:"))
common_prime_dividers = list(set(get_prime_divider(m)) & set(get_prime_divider(n)))
result_gcd = gcd(m,n)
print("Greatest common divider:",result_gcd)
result_lcm = lcm(m,n)
print("Least common multiple:",result_lcm)
#Q3
while True:
    try:
        n= int(input("Enter_n:"))
        break
    except ValueError:
        print("Invalid number")
binary_format = bin(n)[2:]
print(f"binary format of {n} is :",binary_format)
n_str = str(n)
digit_caculate = sum(int(digit) for digit in n_str)
print(f"sum of digits in {n}:",digit_caculate)
reverse = int(str(n)[::-1])
print(f"reverse of {n}:",reverse)
#Q4
while True:
    n=int(input("type_n:"))
    m=int(input("type_m:"))
    if m > n:
        break
    else:
        print("re_enter")
def palindrome_sequence(m,n):
    sequence = list(range(m,n+1))
    palindrome_sequence = sequence + sequence[::-1][1:]
    return palindrome_sequence
result = palindrome_sequence(m,n)
print(result)


        



        