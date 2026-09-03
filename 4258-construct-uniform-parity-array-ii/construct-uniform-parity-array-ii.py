class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)

        if n == 1:
            return True

        nums1.sort()

        # Try making everything odd
        possible_odd = True

        for i in range(n):
            if nums1[i] % 2 == 0:
                # Need an odd smaller number
                found = False
                for j in range(i):
                    if nums1[j] % 2 == 1:
                        found = True
                        break

                if not found:
                    possible_odd = False
                    break

        if possible_odd:
            return True

        # Try making everything even
        possible_even = True

        for i in range(n):
            if nums1[i] % 2 == 1:
                # Need an odd/even choice that gives even.
                # An odd number minus an odd smaller number = even.
                found = False
                for j in range(i):
                    if nums1[j] % 2 == 1:
                        found = True
                        break

                if not found:
                    possible_even = False
                    break

        return possible_even