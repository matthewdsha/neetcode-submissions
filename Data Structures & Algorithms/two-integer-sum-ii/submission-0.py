class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            partner = numbers[r] + numbers[l]
            if partner > target:
                r -= 1
            elif partner < target:
                l += 1
            else:
                return [l+1, r+1]