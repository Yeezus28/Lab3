print("Lab 3 - Software Unit Testing with PyTest")

SORT_ASCENDING = 0
SORT_DESCENDING = 1


def bubble_sort(arr, sorting_order):
    if not all(isinstance(i, int) for i in arr):
        return 2

    # Copy input list to results list
    arr_result = arr.copy()

    # Get number of elements in the list
    n = len(arr_result)

    if n == 0:
        return 0  # Return 0 for empty array
    elif n >= 10:
        return 1  # Return 1 for arrays with 10 or more elements

    # Continue with the bubble sort for arrays with fewer than 10 elements
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if sorting_order == SORT_ASCENDING:
                if arr_result[j] > arr_result[j + 1]:
                    arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]
            elif sorting_order == SORT_DESCENDING:
                if arr_result[j] < arr_result[j + 1]:
                    arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]
            else:
                return []  # Return an empty array if the sorting order is invalid

    return arr_result


