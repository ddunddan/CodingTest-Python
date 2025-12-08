def solution(nums):
    hubo = []
    
    for i in range(len(nums)):
        if nums[i] in hubo:
            pass
        else:
            hubo.append(nums[i])
            
    if len(hubo) <= len(nums) // 2:
        return len(hubo)
    else:
        return len(nums) // 2
