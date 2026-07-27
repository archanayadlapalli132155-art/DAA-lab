import time

def merge_sort(arr):
    # Base case: A list of 0 or 1 elements is already sorted
    if len(arr) <= 1:
        return arr
        
    # Find the middle point to split the array into two halves
    mid = len(arr) // 2
    
    # Recursively split and sort both halves
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    # Merge the sorted halves and return the result
    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr = []
    i = j = 0
    
    # Compare elements from both halves and merge them in order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
            
    # If there are any remaining elements in the left half, add them
    while i < len(left):
        sorted_arr.append(left[i])
        i += 1
        
    # If there are any remaining elements in the right half, add them
    while j < len(right):
        sorted_arr.append(right[j])
        j += 1
        
    return sorted_arr

# --- User Input Section ---
if __name__ == "__main__":
    # Request numbers from the user separated by spaces
    user_input = input("Enter numbers separated by spaces (e.g., 5 2 9 1 7): ")
    
    # Convert the string input into a list of integers
    try:
        numbers = [int(x) for x in user_input.split()]
        
        print("\nOriginal List:", numbers)
        
        # Record the time right before starting the sort
        start_time = time.perf_counter()
        
        # Run the sorting algorithm
        sorted_list = merge_sort(numbers)
        
        # Record the time right after the sort finishes
        end_time = time.perf_counter()
        
        # Calculate execution time (End - Start)
        execution_time = end_time - start_time
        
        # Print Results
        print("Sorted List:  ", sorted_list)
        print(f"Execution Time: {execution_time:.6f} seconds")
        
        # --- Time Complexity Info ---
        print("\n--- Time Complexity Analysis ---")
        print("Best Case: O(n log n)")
        print("Average Case: O(n log n)")
        print("Worst Case: O(n log n)")
        print("\nNote: Unlike Quick Sort, Merge Sort is highly predictable.")
        print("It guarantees O(n log n) performance even in its absolute worst case.")
        
    except ValueError:
        print("Please enter valid integers separated by spaces.")