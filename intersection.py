def intersection(A,B,m,n):
i,j=0,0
A=sorted(A)
B=sorted(B)
res=[]
while(i<m and j<n):
   a,b=A[i],B[j]
   if(a==b):
     res.append(a)
   i=i+1
   j=j+1
   elif(a<b):
     i=i+1
   else:
    j=j+1
return res
A=[1,2,4,5,6]
B=[2,3,5,7,1]
m=len(A)
n=len(B)
intersection(A,B,m,n)
  
