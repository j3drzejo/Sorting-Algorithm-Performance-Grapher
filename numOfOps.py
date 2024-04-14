import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    dominant_operations = 0
    for i in range(n):
        for j in range(0, n-i-1):
            dominant_operations += 1  # Increment dominant operation count
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return dominant_operations

def insertion_sort(arr):
    dominant_operations = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            dominant_operations += 1  # Increment dominant operation count
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return dominant_operations

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    dominant_operations = 0
    for j in range(low, high):
        dominant_operations += 1  # Increment dominant operation count
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1, dominant_operations

def quick_sort(arr, low, high):
    dominant_operations = 0
    if low < high:
        pi, ops = partition(arr, low, high)
        dominant_operations += ops
        dominant_operations += quick_sort(arr, low, pi - 1)
        dominant_operations += quick_sort(arr, pi + 1, high)
    return dominant_operations

def heapify(arr, n, i):
    dominant_operations = 0
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    dominant_operations += 1  # Increment dominant operation count
    if l < n and arr[l] > arr[largest]:
        largest = l

    dominant_operations += 1  # Increment dominant operation count
    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        dominant_operations += heapify(arr, n, largest)

    return dominant_operations

def heap_sort(arr):
    n = len(arr)
    dominant_operations = 0
    for i in range(n // 2 - 1, -1, -1):
        dominant_operations += heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        dominant_operations += heapify(arr, i, 0)
    return dominant_operations

def floyd_heapify(arr, n, i):
    dominant_operations = 0
    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i

        dominant_operations += 1  # Increment dominant operation count
        if left < n and arr[left] < arr[smallest]:
            smallest = left

        dominant_operations += 1  # Increment dominant operation count
        if right < n and arr[right] < arr[smallest]:
            smallest = right

        if smallest == i:
            break

        arr[i], arr[smallest] = arr[smallest], arr[i]
        i = smallest
        dominant_operations += 1

    return dominant_operations

def floyd_heap_sort(arr):
    n = len(arr)
    dominant_operations = 0
    for i in range(n // 2 - 1, -1, -1):
        dominant_operations += floyd_heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        dominant_operations += floyd_heapify(arr, i, 0)
    return dominant_operations

def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

def main():
    sizes = list(range(100, 2001, 50))
    bubble_dominant_ops = []
    insertion_dominant_ops = []
    quicksort_dominant_ops = []
    heap_williams_dominant_ops = []
    heap_floyd_dominant_ops = []

    for size in sizes:
        arr = generate_random_array(size)
        bubble_arr = arr.copy()
        insertion_arr = arr.copy()
        quicksort_arr = arr.copy()
        heap_williams_arr = arr.copy()
        heap_floyd_arr = arr.copy()

        bubble_ops = bubble_sort(bubble_arr)
        insertion_ops = insertion_sort(insertion_arr)
        quicksort_ops = quick_sort(quicksort_arr, 0, len(quicksort_arr)-1)
        heap_williams_ops = heap_sort(heap_williams_arr)
        heap_floyd_ops = floyd_heap_sort(heap_floyd_arr)

        bubble_dominant_ops.append(bubble_ops)
        insertion_dominant_ops.append(insertion_ops)
        quicksort_dominant_ops.append(quicksort_ops)
        heap_williams_dominant_ops.append(heap_williams_ops)
        heap_floyd_dominant_ops.append(heap_floyd_ops)

    plt.plot(sizes, bubble_dominant_ops, label='Bubble Sort')
    plt.plot(sizes, insertion_dominant_ops, label='Insertion Sort')
    plt.plot(sizes, quicksort_dominant_ops, label='Quicksort')
    plt.plot(sizes, heap_williams_dominant_ops, label='Heap (Williams)')
    plt.plot(sizes, heap_floyd_dominant_ops, label='Heap (Floyd)')
    plt.xlabel('Number of Elements')
    plt.ylabel('Number of Dominant Operations')
    plt.title('Sorting Algorithm Dominant Operation Performance')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
