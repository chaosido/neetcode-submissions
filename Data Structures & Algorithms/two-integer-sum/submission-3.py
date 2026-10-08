class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            new_target = target - nums[i]
            for j in range(i + 1, len(nums)):
           
                if nums[i] + nums[j] == target: 
                    idx_list = [i, j]
                    return idx_list
                    return idx_list

        