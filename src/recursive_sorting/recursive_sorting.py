# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # Will take the smaller value from arrA[0], arrB[0], 
    # then it will pop that smaller value to the merged array
    # arrA and arrB will get smaller until they are both empty
    for i in range(0, len(merged_arr)):
        print("i, arrA, arrB, merged_arr", i, arrA, arrB, merged_arr)
        
        if arrA != [] and arrB != []:
            if arrA[0] < arrB[0]:
                merged_arr[i] = arrA[0]
                arrA.pop(0)
            elif arrA[0] > arrB[0]:
                merged_arr[i] = arrB[0]
                arrB.pop(0)
        else:
            if arrA != [] and arrB == []:
                merged_arr[i] = arrA[0]
                arrA.pop(0)
            elif arrB != [] and arrA == []:
                merged_arr[i] = arrB[0]
                arrB.pop(0)       
    
    print("merged_arr FINISH*********************", merged_arr)
    return merged_arr

def s_merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    # TO-DO
    i, j, merged_arr = 0, 0, []
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr.append(arrA[i])
            i += 1
        else:
            merged_arr.append(arrB[j])
            j += 1
    merged_arr.extend(arrA[i:])
    merged_arr.extend(arrB[j:])
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # Take in the array, split it in half until it is an array of [1]
    if len(arr) <= 1:
        return arr 

    middle = len(arr)//2
    left = arr[:middle]
    right = arr[middle:]

    print("left, right", left, right)
    return s_merge(merge_sort(left), merge_sort(right))


# [10] [4]
arrA = [10, 8, 6, 1]
arrB = [6]
arrD = [1]

arrC = [10, 4, 8, 2, 6, 1]
arrE = [99, 1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# print(merge( arrB, arrD ))
print("end:", merge_sort( arrA ))

# print(len(arrA)//2)

# elements = len( arrA ) + len( arrB )
# merged_arr = [0] * elements

# print("elements", elements)
# print("merged_arr", merged_arr)



# STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr

# def merge_sort_in_place(arr, l, r): 
#     # TO-DO

#     return arr


# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort( arr ):

#     return arr
