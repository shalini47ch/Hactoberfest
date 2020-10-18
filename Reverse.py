def reverse(arr,n):
    start=0
	end=n-1
	while(start<end):
	  temp=arr[start]
	  arr[start]=arr[end]
	  arr[end]=temp
	 return arr
