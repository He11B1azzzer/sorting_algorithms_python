import math

def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def shell_sort(arr, length):
    dist = int(length / 2)
    while dist > 0:
        for i in range(int(length - dist)):
            j = i
            while j >= 0 and arr[j] > arr[int(j + dist)]:
                arr[j], arr[int(j + dist)] = arr[int(j + dist)], arr[j]
                j -= 1
        d = int(dist / 2)
    return arr


def quik_sort(arr,first,last):
    f = first
    l = last
    pivot = arr[int((f + l) / 2)]
    while f <= l:
        while arr[f] < pivot:
            f += 1
        while arr[l] > pivot:
            l -= 1
        if f <= l:
            arr[f], arr[l] = arr[l], arr[f]
            f += 1
            l -= 1
    if first < l:
        quik_sort(arr,first,l)
    elif f < last:
        quik_sort(arr,f,last)
    return arr


def insertion_sort(arr):
    for i in range(len(arr) - 1):
        j = i - 1
        key = arr[i]
        while arr[j] > key and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def batcher_sort(arr):
    t = int(math.log(len(arr),2))
    p = 2 ** (t - 1)
    while p > 0:
        q = 2 ** (t - 1)
        r = 0
        d = p
        while q >= p:
            i = 0
            while i < len(arr) - d:
                if arr[i] > arr[i + d]:
                    arr[i], arr[i + d] = arr[i + d], arr[i]
                i += 1
            d = q - p
            q = int(q / 2)
            r = p
        p = p // 2
    return arr