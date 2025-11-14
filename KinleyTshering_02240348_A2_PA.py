# Part A:Searching Algorithms Implementation
#  This program allows users to perform linear and binary searches on lists of students IDs and test scores.
#1. Linear Search- find a student ID
# Searchs for a target value in an unsorted list using linear search algorithm.
def linear_search(student_ids, target):
    """Perform linear search on the list of students IDs."""
    comparisons = 0 # counter to track number of comparisons made
    for i in range(len(student_ids)):
        comparisons += 1
        # check if current element matches the target
        if student_ids[i] == target:
            return i + 1, comparisons # Return position (1-indexed) and comparisons
    # if not found , return -1 amd comparisons
    return -1, comparisons

#2. Binary Search - Find a Score
# searches for a tartget value in a sorted list using the binary search algorithm.
def binary_search(scores, target):
    low = 0 # starting index
    high = len(scores) - 1 # ending index
    comparisons = 0 # counter for comparisons

    # repeat while the search range is valid
    while low <= high:
        comparisons += 1
        mid = (low + high) // 2 # find the middle index
        if scores[mid] == target:
            return mid + 1, comparisons # if the target matches middle, return (1-indexed)
        elif scores[mid] < target:
            low = mid + 1 # if the target larger, search the right half
        else:
            high = mid - 1 # if the target smaller, search the left half

    return -1, comparisons # if not found, return -1 and comparisons

# this function provides a comand-line interface for the user to choose and run different search algorithms.
def main():
    student_ids = [2000, 2001, 2002, 1008, 1003, 2010, 1004, 1009, 1007, 2012, 1011, 1013, 2214, 1015, 3016, 1017, 2018, 1019, 1020, 1021] # unsorted list of 20 student IDs
    sorted_scores = [45, 52, 58, 63, 67, 72, 75, 78, 82, 85, 88, 90, 92, 95, 98, 100, 105, 108, 110, 115]# sorted list of 20 test scores

    # main loop to show the the menu until user exits.

    while True:
        #display menu options
        print("Searching Algorithms Menu")
        print("Select a search operation (1-3):")
        print("1. Linear search - Find Student id")
        print("2. Binary Search - find score")
        print("3. Exit program")

        choice = input("enter your choice: ")
        
        if choice == '1':
            print(f"\nSearching in the list: {student_ids}")
            try:
                # ask user to enter a target ID to search
                target = int(input("Enter Student ID to search: "))

                # perform the linear search
                position, comparisons = linear_search(student_ids, target)
                if position != -1:
                    print(f"Result: Student ID {target} found at position {position}")
                else:
                    print(f"Result: Student ID {target} not found")
                print(f"Comparisons made: {comparisons}")
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        elif choice == '2': # binary search
            print(f"\nSorted scores: {sorted_scores}")
            try:
                target = int(input("Enter score to search: "))
                position, comparisons = binary_search(sorted_scores, target)
                if position != -1:
                    print(f"Result: Score {target} found at position {position}")
                else:
                    print(f"Result: Score {target} not found")
                print(f"Comparisons made: {comparisons}")
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        elif choice == '3':
            print("Thank you for using the search program!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 3.")

        again = input("\nWould you like to perform another search? (y/n): ").lower()
        if again != 'y':
            print("Thank you for using the program!")
            break


if __name__ == "__main__":
    main()

        