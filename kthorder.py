import random
import time
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(sys.getrecursionlimit() * 4)
def partition(b,v):
    #print("B V",b,v)
    if len(b) == 1:
        return b, 0
    elif len(b) == 2:
        return [b[0] if b[0] < b[1] else b[1], b[1] if b[0] < b[1] else b[0]], 0 if b[0] == v else 1
    else:
        mark = -1
        a= list(b)
        lmost = 0
        for i in range(len(a)):
            if(a[i] < v):
                tmp = a[lmost]
                a[lmost] = a[i]
                a[i] = tmp
                if lmost == mark:
                    mark = i
                lmost += 1
                
            else:
                if v == a[i]:
                    mark = i

            #print(a, lmost)

        a[mark] = a[lmost]
        a[lmost] = v

        return a,lmost

def kth_order(a, k):
    ap = list(a)
    medians = []
    for i in range(len(a)//5):
        medians.append(sorted(ap[i*5:(i+1)*5])[2])
   
    extra = sorted(ap[len(a)//5 * 5: len(a)//5 * 5 + len(a) % 5])
    if len(extra) != 0:
        medians.append(extra[len(extra)//2])



    #if()
    pivot = None
    #print(medians)
    if(len(medians) > 1):
        pivot = kth_order(medians, len(medians) // 2)

    else:
        pivot = medians[0]
    #print("piv",pivot)
    
    ap, lm = partition(a, pivot)
    #print(ap)
    #print("piv, ap, lm, order",pivot, ap, lm, k)
    if (k == lm):
        return ap[lm]
    if k < lm:
        return kth_order(ap[:lm], k)
    else:
        return kth_order(ap[lm:], k - lm)
    
    #if 


#print(time.time_ns())
times_alg = []
times_sort = []
#kth_order([421,21,422,433,99,98,94,87,32,499,98,12,13,14,15,3,1],3)
g = [421,21,422,433,199,18,94,87,32,1499,98,122,1333,1114,315,33,1]
print(partition(g,98))
gp = []

for i in range(len(g)):
    gp.append(kth_order(g, i))
print("GPG",gp,"\n",sorted(g))
print(kth_order(g, 8))
print(sorted(g)[6])
print(sorted(g))
input()
ns = []
for i in range(1,40,1):
    ao = 0
    aa = 0
    ns.append(i)
    for k in range(100):
        
        vals = []
        for j in range(i):
            vals.append(random.randint(-99900,91200))
        order = i//4

        ts = time.time_ns()
        stat = kth_order(vals, order)
        tf = time.time_ns()

        aa+=(tf - ts)

        ts = time.time_ns()
        if stat != sorted(vals)[order]:
            print(stat,sorted(vals)[order],i)
            raise Exception("Kth order algorithm failed")
        tf = time.time_ns()

        ao +=(tf - ts)
    times_sort.append(ao)
    times_alg.append(aa)
    #print(vals)

plt.plot(ns, times_alg, label = "alg")
plt.plot(ns, times_sort)
plt.legend()
plt.show()