from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer: List[List[int]] = []
      # we sort to easily avoid duplicates and we can't do better than O(n^2) anyways
        nums.sort()

        # Since we need at least 3 numbers so go only upto len - 2 (leaving space for 2 ahead)
        for i in range(len(nums) - 2):
          # if current value > 0 we can't have a sum of 0 since array is sorted and we only look ahead
            if nums[i] > 0: 
              break

           # Skip duplicates - we don't want to start with the same combination
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 2 pointers for 2 sum essentially
            left = i + 1
            right = len(nums) - 1
            while (left < right):
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum < 0:
                    left += 1
                elif curr_sum > 0:
                    right -= 1
                else:
                    answer.append([nums[i], nums[left], nums[right]])
                   # we increase both left and right since this was the only combination of these numbers that could sum to 0
                    left += 1
                    right -= 1
                  # skip duplicates inside of the loop as well
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        
        return answer





                
        
