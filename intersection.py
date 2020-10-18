def intersection(A,B,m,n):
i,j=0,0
res=[]
while(i<m and j<n):
 if(A[i]==B[j]):
   res.append(A[i])
   i=i+1
   j=j+1
  elif(A[i]<B[j]):
  i=i+1
  else:
  j=j+1
  return res
  