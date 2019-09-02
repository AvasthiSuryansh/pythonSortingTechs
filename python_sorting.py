from random import randint

def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1],nums[i]
                swapped = True
    print('Sorted array using Bubble Sort is: {}'.format(nums))


def selection_sort(nums):
    for i in range(len(nums)):
        minpos = i
        for j in range(i+1,len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j
        nums[i],nums[minpos] = nums[minpos], nums[i]

    print('Sorted array using Selection Sort is: {}'.format(nums))



def insertion_sort(nums):
    for i in range(1,len(nums)):
        for j in range(i-1,0,-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
            else:
                break
    print('Sorted array using Insertion Sort is: {}'.format(nums))


def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    midpoint = len(nums)//2
    left,right = nums[:midpoint],nums[midpoint:]
    return merge(left,right)

def merge(left,right):

    result = []
    left_pointer = right_pointer = 0

    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1

    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])

    print('Sorted array using Merge Sort is: {}'.format(result))


def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[randint(0,len(nums)-1)]

    smaller,equal,larger = [], [], []

    for i in nums:
        if i<pivot:
            smaller.append(i)
        elif i == pivot:
            equal.append(i)
        else:
            larger.append(i)
    return quick_sort(smaller)+equal+quick_sort(larger)

def main():
    unsorted_numbers = [4, 3, 2, 5, 6, 7, 1, 3, 23, 1, 22, 6]
    print(unsorted_numbers)
    bubble_sort(unsorted_numbers)
    selection_sort(unsorted_numbers)
    insertion_sort(unsorted_numbers)
    merge_sort(unsorted_numbers)
    s = quick_sort(unsorted_numbers)
    print("Sorted array using Quick Sort is {}".format(s))

if __name__ == '__main__':
    main()
