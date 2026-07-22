#Longest Increasing Subsequence

def max_lis (nums):
    n= len(nums)
    if n ==0:
        print('555555555')
        return 0
    assistant = n*[1]
    for i in range(n):
        for j in range(i):
             if nums[i]> nums[j]:
                 assistant[i]= max(assistant[i], assistant[j]+1)
    return max(assistant)
numbers = [1,2,3,4,5,9,11,6,7,8,10,15]
