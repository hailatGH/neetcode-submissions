from typing import List

def custom_bubble_sort(vals: list, reverse: bool = False) -> list:
    n = len(vals)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if (vals[j] < vals[j + 1]) if reverse else (vals[j] > vals[j + 1]):
                vals[j], vals[j + 1] = vals[j + 1], vals[j]
                swapped = True
        if not swapped:
            break
    return vals

def sort_words(words: List[str]) -> List[str]:
    words.sort(reverse=True)
    return custom_bubble_sort(words, True)

def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(reverse=True)
    return numbers

def sort_decimals(numbers: List[float]) -> List[float]:
    numbers.sort(reverse=True)
    return numbers

# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))
