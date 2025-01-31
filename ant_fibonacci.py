def antfibo(a,b,n):
    if (n==0):
        return a
    elif (n == 1):
        return b
    elif ((n/2)%2==1):
        return antfibo(a,b,n-1)+antfibo(a,b,n-2)
    else:
        return antfibo(a,b,n-1)-antfibo(a,b,n-4)

Q = int(input())

for _ in range(Q):
    a,b,n = map(int,input().split())
    print(antfibo(a,b,n))