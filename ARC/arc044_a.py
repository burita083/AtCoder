def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def digitsum(n):
    array = list(map(int, str(n)))
    return sum(array)

N = int(input())
if N == 1:
    print("Not Prime")
    exit()
if is_prime(N):
    print("Prime")
    exit()

S = str(N)
if int(S[-1]) % 2 != 0 and int(S[-1]) != 5 and digitsum(N) % 3 != 0:
    print("Prime")
    exit()
print("Not Prime")