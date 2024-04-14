import time
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def floyd_heapify(arr, n, i):
    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i

        if left < n and arr[left] < arr[smallest]:
            smallest = left

        if right < n and arr[right] < arr[smallest]:
            smallest = right

        if smallest == i:
            break

        arr[i], arr[smallest] = arr[smallest], arr[i]
        i = smallest

def floyd_heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        floyd_heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        floyd_heapify(arr, i, 0)

def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time

def main():
    sizes = list(range(1, 2001, 50))
    bubble_times = []
    insertion_times = []
    quicksort_times = []
    heap_williams_times = []
    heap_floyd_times = []

    for size in sizes:
        arr = generate_random_array(size)
        bubble_arr = arr.copy()
        insertion_arr = arr.copy()
        quicksort_arr = arr.copy()
        heap_williams_arr = arr.copy()
        heap_floyd_arr = arr.copy()

        bubble_time = measure_time(bubble_sort, bubble_arr)
        insertion_time = measure_time(insertion_sort, insertion_arr)
        quicksort_time = measure_time(lambda x: quick_sort(x, 0, len(x)-1), quicksort_arr)
        heap_williams_time = measure_time(heap_sort, heap_williams_arr)
        heap_floyd_time = measure_time(floyd_heap_sort, heap_floyd_arr)

        bubble_times.append(bubble_time)
        insertion_times.append(insertion_time)
        quicksort_times.append(quicksort_time)
        heap_williams_times.append(heap_williams_time)
        heap_floyd_times.append(heap_floyd_time)

        print(f"Size: {size}, Bubble Sort: {bubble_time:.6f} seconds, Insertion Sort: {insertion_time:.6f} seconds, Quicksort: {quicksort_time:.6f} seconds, Heap (Williams): {heap_williams_time:.6f} seconds, Heap (Floyd): {heap_floyd_time:.6f} seconds")

    plt.plot(sizes, bubble_times, label='Bubble Sort')
    plt.plot(sizes, insertion_times, label='Insertion Sort')
    plt.plot(sizes, quicksort_times, label='Quicksort')
    plt.plot(sizes, heap_williams_times, label='Heap (Williams)')
    plt.plot(sizes, heap_floyd_times, label='Heap (Floyd)')
    plt.xlabel('Number of Elements')
    plt.ylabel('Time Taken (seconds)')
    plt.title('Sorting Algorithm Performance')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
