#User function Template for python3

class Solution:
    ##Complete this code
    def countOnes(self,arr, N):
        #Your code here
        '''count = 0
        for i in arr:
            if i == 1:
                count += 1
        return count'''
        low = 0
        high = N - 1
        count = 0
        while low <= high:
            mid = (low + high)//2
            
            if arr[mid] == 1:
                low = mid + 1
            elif arr[mid] == 0:
                high = mid - 1
                
            else:
                if mid == 0 or arr[mid - 1] != arr[mid]:
                    return mid
                else:
                    high = mid - 1
        return low
                
                
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3