### Bài này đề bài yêu cầu input là một số, chứ ko phải một mảng nha chú ơi.

arr=[1,1,1]
for i in range(0,len(arr)): arr[i]=input('nhap so thu '+str(i)+':')
for i in range(0,len(arr)):
    if int(arr[i])%2==0:
        print(str(arr[i])+' la so chan')
    else:
        print(str(arr[i])+' la so le')
