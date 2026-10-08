class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = defaultdict(int)
        for idx in nums:
            counter[idx] += 1
            if counter[idx] > 1:
                return True

        
        return False 


         