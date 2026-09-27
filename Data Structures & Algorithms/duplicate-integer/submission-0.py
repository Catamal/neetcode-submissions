class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i = []
        j = 0
        while j < len(nums):
            if nums[j] in i:
                return True
            i.append(nums[j])
            j += 1
        return False
            