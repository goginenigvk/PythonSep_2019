class Solution:   
    def climbStairs(self, A): #9,9  
        if A>1:
            res = [0 for i in range (A+1)] #0 0 0 0
        elif A==1:
            return 1
        res[0]=1
        res[1]=1
        for i in range(2,A+1):
            j=1
            print(i,j)
            while j<=2 and j<=i:
                res[i] = res[i] + res[i-j]
                
                j=j+1
                print(res)
                print(i,j)
        return res[A]

A=int(input("Enter A:"))
var=Solution.climbStairs(A,A)
print(var)