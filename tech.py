from collections import deque
def maxslidingwindow(nums,K):
    dq=deque()
    result=[]
    
    for i in range(len(nums)):
        if dq and dq[0]== i-k:
            dq.popleft()
            while dq and num [dq[-1]]<nums[i]:
            
             dp.pop()
            dq.appent(i)
            if i>=k-1:
              results.append(nums[dq[0]])
            return result 
        nums=[1,2,-1,-3,5,3,6,7,]
        k=3
        print(maxslidingwindow(nums,k))        
