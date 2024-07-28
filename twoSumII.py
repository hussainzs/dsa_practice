class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
      # Use 2 pointers since sorted
        left = 0
        right = len(numbers) - 1

      # left >= right invalid because that would start counting duplicates
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum < target:
              # sum too small -> we need larger numbers so left ++ since sorted
                left += 1
            elif sum > target:
              # sum too large -> we need smaller numbers so right -- since sorted
                right -= 1
            else:
              # found our answer
                return [left + 1, right + 1]
