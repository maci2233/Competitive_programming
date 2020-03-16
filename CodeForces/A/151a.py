n,k,l,c,d,p,nl,np = [int(i) for i in input().split()]
a1 = (k*l)//nl
a2 = c*d
a3 = p//np
print(str(min(a1,a2,a3)//n))
