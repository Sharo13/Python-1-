 # bubble sort
def bubble_sort(arr):
    l = len(arr)
    for i in range(l):
        for j in range(0, l-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        
lst = [94, 56, 32, 55, 344, 192, 4832, 2, 9, 0, 1]
bubble_sort(lst)
print("Sorted array:", lst)

 # merge sort

def merge_sort(arr):
    if len(arr) > 1:
        l = len(arr)//2
        y = arr[:l]
        x = arr[l:]

        merge_sort(y)
        merge_sort(x)
        i = j = k = 0

        while i < len(y) and j < len(x):
            if y[i] < x[j]:
                arr[k] = y[i]
                i += 1
            else:
                arr[k] = x[j]
                j += 1
            k += 1

        while i < len(y):
            arr[k] = y[i]
            i += 1
            k += 1

        while j < len(x):
            arr[k] = x[j]
            j += 1
            k += 1

lst = [94, 56, 32, 55, 344, 192, 4832, 2, 9, 0, 1]
merge_sort(lst)
print("Sorted array:",lst)

#insertion sort
def insertion_sort(arr):
    l = len(arr)  
      
    if l == 1 or l == 0:
        return  
    for i in range(1, l): 
        k = arr[i]  
        j = i-1
        while j >= 0 and k < arr[j]:  
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = k  
  
  
lst = [94, 56, 32, 55, 344, 192, 4832, 2, 9, 0, 1]
insertion_sort(lst)
print("Sorted array:",lst)
