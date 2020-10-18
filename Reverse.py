def reverse(arr,n):
    start=0
    end=n-1
    while(start<end):
	 temp=arr[start]
	 arr[start]=arr[end]
	 arr[end]=temp
     return arr
arr=[1,4,6,8]
n=len(arr)
reverse(arr,n)
#did proper indendation
