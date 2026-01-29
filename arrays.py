def insert_element(arr, element):
    arr.append(element)
    return arr

def delete_element(arr, element):
    if element in arr:
        arr.remove(element)
    return arr

def reverse_array(arr):
    return arr[::-1]

def find_max_min(arr):
    return max(arr), min(arr)

def remove_duplicates(arr):
    return list(set(arr))
