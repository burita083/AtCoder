N = int(input())

left = 0
remain = N
l = []
for i in range(1, N+1):
    left += i
    remain = N-left
    if remain-i-1==0:
        print(i+1)
        exit()
    else:
        print(remain, left, "aaa")
        if remain < left:
            print(remain+i)
            exit()
        print(i)



    