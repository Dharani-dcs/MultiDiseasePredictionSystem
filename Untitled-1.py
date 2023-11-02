arr=[1,2,3,4]
n=len(arr)
pref=[0]*n
suff=[0]*n

su=arr[0]
for i in range(1,n):
    pref[i]=su
    su+=arr[i]
su=arr[-1]
for i in range(n-2,-1,-1):
    suff[i]=su
    su+=arr[i]

result=[0]
for i in range(n):
    total=abs(pref[i]-suff[i])
    if total==1:
        result.append(i+1)
print(max(result))

