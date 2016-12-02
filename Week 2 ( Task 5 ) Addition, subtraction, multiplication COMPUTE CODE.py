A = [[3,2,6],
    [7 ,3,8],
    [2 ,4,7]]

B = [[7,2,3],
    [4,5,9],
    [2,4,5]]

C = [[6,3,2],
    [7,5,9],
    [1,7,4]]

answer = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# goes through the rows
for i in range(len(A)):
   # goes through the columns
   for j in range(len(A[0])):
       answer[i][j] = A[i][j] = B[i][j]*C[i][j]-2*(B[i][j]+C[i][j])

for n in answer:
   print(n)

#calculates the run time of the code above
import timeit

start = timeit.default_timer()

stop = timeit.default_timer()

print (stop - start) 
