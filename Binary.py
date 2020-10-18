def binarysearch(arr,n,ele):
  
  start=0
  end=n-1
   while(start<=end):
     mid=(start+end)//2
   if(ele==arr[i]):
     return mid
   elif(ele<arr[mid]):
     end=mid-1
   else:
     end=mid+1
arr=[2,3,6,8]
n=len(arr)
ele=3
binarysearch(arr,n,ele)

  
   
