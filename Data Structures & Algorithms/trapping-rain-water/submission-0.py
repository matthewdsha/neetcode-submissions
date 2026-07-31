class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxWater = 0
        leftMax, rightMax = height[l], height[r]

        while l <= r:
            if leftMax < rightMax:
                water = leftMax - height[l]
                leftMax = max(leftMax, height[l])
                l += 1
                if water > 0:
                    maxWater += water
            else:
                water = rightMax - height[r]
                rightMax = max(rightMax, height[r])
                r -= 1
                if water > 0:
                    maxWater += water
            
        return maxWater
            