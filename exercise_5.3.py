class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        Сперва сделал при помощи метода sort(), но потом переделал без его использования
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = []
        i = 0
        j = 0
        if len(nums1) == 0:
            nums3 = nums2
        elif len(nums2) == 0:
            nums3 = nums1
        else:
            while True:
                if nums1[i] <= nums2[j]:
                    nums3.append(nums1[i])
                    i += 1
                    if i == len(nums1):
                        nums4 = nums2[j:]
                        nums3 = nums3 + nums4
                        break
                elif nums1[i] >= nums2[j]:
                    nums3.append(nums2[j])
                    j += 1
                    if j == len(nums2):
                        nums4 = nums1[i:]
                        nums3 = nums3 + nums4
                        break
        count = len(nums3)
        if count % 2 == 0:
            return (nums3[count//2] + nums3[count//2 - 1]) * 0.5
        else:
            return nums3[count//2]
