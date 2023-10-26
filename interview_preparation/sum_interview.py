# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

from itertools import combinations

nums = [2, 7, 11, 15, 3, 6]
target = 9

target_sum_list = []
ctr_step = 1 

for idx_i in range(len(nums)):
    for idx_j in range(ctr_step, len(nums)):
        if nums[idx_i] + nums[idx_j] == target:
            target_sum_list.append([idx_i, idx_j])
    ctr_step += 1
            
print(target_sum_list)
