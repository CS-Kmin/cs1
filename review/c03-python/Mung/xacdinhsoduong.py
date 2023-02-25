arr=[1,1,1]
for i in range(0,len(arr)): 
    arr[i]=input('nhap so thu '+str(i)+':')
for i in range(0,len(arr)):
    if int(arr[i])>0:
        print(str(arr[i])+' la so duong')
    