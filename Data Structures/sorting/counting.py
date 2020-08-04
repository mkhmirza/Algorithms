#!/usr/bin/python env

a = [1 , 2, 4, 5, 6, 0, 2]
k = max(a)
c = [0 for x in range(k+1)]

# calculate frequency/count
for i in range(0,k+1):
    c[a[i]] += 1
# calculate cummulative frequency
for i in range(0,len(a)):
    c[i] += c[i-1]


b = [0] * len(a)
i = len(a) - 1
# perform actual sorting
while i >= 0:
    b[c[a[i]] - 2] = a[i]
    c[a[i]] -= 1
    i -= 1  

print(f"Original Array: {a}")
print(f"Sorted Data:    {b}")