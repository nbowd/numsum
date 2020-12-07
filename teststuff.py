def twosum(arr, target):
    left = 0
    right = -1
    while right < left:
        curr = arr[left] + arr[right]
        if curr < target:
            left += 1
        elif curr > target:
            right -= 1
        else:
            return [left, right]
    return [-1,-1]

nums1 = [-1,1,2,3,5]
target1 = 5
nums2 = [2,7,11,15]
target2 = 9
nums3 = [2,3,4]
target3 = 6

print(twosum(nums1, target1))
print(twosum(nums2, target2))
print(twosum(nums3, target3))