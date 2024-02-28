arr = [10,20,30,40,50,60,70,80,90]
arr_rotated = [10,20,30,40,50,60,70,80,90,0,1,2,3,4,5,6]
arr_rotated_2 = [3,1]

def binary_search_using_loop(arr: list, ele: int) -> bool:
  low = 0
  high = len(arr)-1
  while low <= high:
    mid = (low + high) // 2
    if arr[mid] == ele:
      return True
    elif ele > arr[mid]:
      low = mid + 1
    elif ele < arr[mid]:
      high = mid - 1
    
  return False

def binary_search(nums,target,low,high):
#   print('low: {}, high: {}, mid: {}'.format(low, high, (low + high)//2))
  if low > high:
    return False
  else:
    mid = (low + high)//2
    if nums[mid] == target:
      return True
    elif nums[mid] < target:
      return binary_search(nums,target,mid+1,high)
    else:
      return binary_search(nums,target,low,mid-1)
    
def modified_binary_search(nums: list, target: int, low: int, high: int) -> bool:
  if low > high:
    return False
  else:
    print('low: {}, high: {}, mid: {}'.format(low, high, (low + high)//2))
    mid = (low + high) // 2
    if nums[mid] == target:
      return True
    if nums[low] < nums[mid]:
      if target >= nums[low] and target < nums[mid]:
        high = mid - 1
        return modified_binary_search(nums=nums, target=target, low=low, high=high)
      else:
        low = mid + 1
        return modified_binary_search(nums=nums, target=target, low=low, high=high)
    else:
      if target > nums[mid] and target <= nums[high]:
        low = mid + 1
        return modified_binary_search(nums=nums, target=target, low=low, high=high)
      else:
        high = mid-1
        return modified_binary_search(nums=nums, target=target, low=low, high=high)
      
def modified_binary_search_using_loop(arr: list, ele:int) -> bool:
  low = 0
  high = len(arr)-1
  while low <= high:
    print('low: {}, high: {}, mid: {}'.format(low, high, (low + high)//2))
    mid = (low + high)//2
    if arr[mid] == ele:
      return True
    if arr[mid] > arr[low]:
      if ele >= arr[low] and ele < arr[mid]:
        high = mid - 1
      else:
        low = mid + 1
    else:
      if ele > arr[mid] and ele <= arr[high]:
        low = mid + 1
      else:
        high = mid - 1
    print('low: {}, high: {}, mid: {}'.format(low, high, (low + high)//2))
  return False

# print(binary_search(nums=arr,target=200,low=0,high=len(arr)-1))
# print(binary_search_using_loop(arr=arr, ele=100))
# print(modified_binary_search(nums=arr_rotated_2, target=1, low=0, high=len(arr_rotated_2)-1))
print(modified_binary_search_using_loop(arr=arr_rotated_2, ele=1))