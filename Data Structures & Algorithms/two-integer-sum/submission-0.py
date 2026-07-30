class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            partner = target - nums[i]
            if partner in map.keys():
                return [map[partner], i]
            map[nums[i]] = i
        
        return [0, 1]