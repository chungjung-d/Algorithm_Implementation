def mergeSort(nums):

    if(len(nums)<=1):  # 배열의 길이가 1개일 때 반환 
        return nums
    
    array_length = len(nums)

    mid = int(array_length/2)

    left_nums = nums[:mid]
    right_nums = nums[mid:]

    left_nums = mergeSort(left_nums)
    right_nums = mergeSort(right_nums)

    sorted_array = []

    while(len(left_nums)!=0 or len(right_nums)!=0):
        if not left_nums:  #(left list가 비었음)
            sorted_array = sorted_array + right_nums
            right_nums.clear()
            continue
        if not right_nums: #(right list가 비었음)
            sorted_array = sorted_array + left_nums
            left_nums.clear()
            continue
        if(left_nums[0]<right_nums[0]):
            sorted_array.append(left_nums[0])
            left_nums.pop(0)
            continue
        if(right_nums[0]<left_nums[0]):
            sorted_array.append(right_nums[0])
            right_nums.pop(0)
            continue
    
    nums = sorted_array

    return nums
        

def findTarget(numArr , target):
    if(target in numArr):
        return numArr.index(target)+1
    
    else:
        for index , i in enumerate(numArr):
            if(i > target):
                return index+1
        return len(numArr)+1


def solve(nums , target):
    numArr = mergeSort(nums)

    output = findTarget(numArr , target)

    print(output)

