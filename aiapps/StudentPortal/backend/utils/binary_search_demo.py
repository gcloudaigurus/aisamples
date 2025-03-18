def iterative_binary_search(arr, target):
    """
    Iterative implementation of binary search.
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def recursive_binary_search(arr, target, left=None, right=None):
    """
    Recursive implementation of binary search.
    Time Complexity: O(log n)
    Space Complexity: O(log n) due to recursion stack
    """
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, right)
    else:
        return recursive_binary_search(arr, target, left, mid - 1)

def binary_search_leftmost(arr, target):
    """
    Binary search that returns the leftmost occurrence of the target.
    Useful when there are duplicate elements.
    """
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left if left < len(arr) and arr[left] == target else -1

def binary_search_rightmost(arr, target):
    """
    Binary search that returns the rightmost occurrence of the target.
    Useful when there are duplicate elements.
    """
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] > target:
            right = mid
        else:
            left = mid + 1
    
    return right - 1 if right > 0 and arr[right - 1] == target else -1

def binary_search_rotated(arr, target):
    """
    Binary search in a rotated sorted array.
    Example: [4,5,6,7,0,1,2] is a rotated sorted array.
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
            
        # Left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target <= arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if arr[mid] <= target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

def main():
    # Test cases
    test_cases = [
        {
            "name": "Basic Binary Search",
            "arr": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "target": 7,
            "expected": 6
        },
        {
            "name": "Element Not Found",
            "arr": [1, 2, 3, 4, 5],
            "target": 6,
            "expected": -1
        },
        {
            "name": "Duplicate Elements",
            "arr": [1, 2, 2, 2, 3, 4, 5],
            "target": 2,
            "expected": 1
        },
        {
            "name": "Rotated Array",
            "arr": [4, 5, 6, 7, 0, 1, 2],
            "target": 0,
            "expected": 4
        }
    ]
    
    # Run tests
    for test in test_cases:
        print(f"\n{test['name']}:")
        print(f"Array: {test['arr']}")
        print(f"Target: {test['target']}")
        
        # Test iterative binary search
        result = iterative_binary_search(test['arr'], test['target'])
        print(f"Iterative Binary Search: Index {result}")
        
        # Test recursive binary search
        result = recursive_binary_search(test['arr'], test['target'])
        print(f"Recursive Binary Search: Index {result}")
        
        # Test leftmost binary search
        result = binary_search_leftmost(test['arr'], test['target'])
        print(f"Leftmost Binary Search: Index {result}")
        
        # Test rightmost binary search
        result = binary_search_rightmost(test['arr'], test['target'])
        print(f"Rightmost Binary Search: Index {result}")
        
        # Test rotated binary search if applicable
        if "Rotated" in test['name']:
            result = binary_search_rotated(test['arr'], test['target'])
            print(f"Rotated Binary Search: Index {result}")

if __name__ == "__main__":
    main() 