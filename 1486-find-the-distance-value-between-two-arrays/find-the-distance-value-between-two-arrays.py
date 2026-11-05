class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        cnt=0
        for x in arr1:
            found=False
            for y in arr2:
                if abs(x-y)<=d:
                    found=True
                    break
            if not found:
                cnt+=1
        return cnt