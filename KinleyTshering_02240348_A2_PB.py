# Part B: Sorting Algorithms Implementations
# Implements bubble sort, insertion sort, and quick sort
# Bubble sort-Sort student Names
# sorts a list of names alphabetically using bubbke sort
def bubble_sort(names):
    n = len(names)
    # make a copy so the original list remains unchanged
    sorted_names = names.copy()

    # Outer loop for each pass
    for i in range(n - 1):
        # inner loop for comparing adjacent elements
        for j in range(n - 1):
            if sorted_names[j] > sorted_names[j + 1]:
                sorted_names[j], sorted_names[j + 1] = sorted_names[j + 1], sorted_names[j]

    return sorted_names

# Insertion Sort - Sort Test scores
# sorts a list of numbers (scores) using Insertion sort

def insertion_sort(scores):
    sorted_scores = scores.copy()

    for i in range(1, len(sorted_scores)):
        key = sorted_scores[i]
        j = i - 1

        while j >= 0 and sorted_scores[j] > key:
            sorted_scores[j + 1] = sorted_scores[j]
            j -= 1

        sorted_scores[j + 1] = key

    return sorted_scores

# Quick Sort - Sort book prices
# sorts a list of prices using quick sort recursively returns both sorted list and number of recursive calls made

def quick_sort(prices, depth=0):
    # track the number of recursive calls
    if len(prices) <= 1:
        return prices, 1
    
    pivot = prices[len(prices) // 2] # choose the middle element as pivot
    left = [x for x in prices if x < pivot]
    middle = [x for x in prices if x == pivot]
    right = [x for x in prices if x > pivot]

    sorted_left, left_calls = quick_sort(left, depth + 1)
    sorted_right, right_calls = quick_sort(right, depth + 1)

    total_calls = 1 + left_calls + right_calls
    return sorted_left + middle + sorted_right, total_calls

# main
# provides the main user menu and handles sorting operations

def main():
    # Hardcoded lists for testing
    student_names = ["Kado", "Bobchu", "Zamu", "Nado", "Lemo", "Tashi", "Mina", "Dorji", "Pema", "Sonam", "Kezang", "Namgay", "Choki", "Ugyen", "Dechen"]

    test_scores = [78, 45, 92, 67, 88, 54, 73, 82, 91, 59, 76, 85, 48, 93, 71, 89, 57, 80, 69, 62]

    book_prices = [450, 230, 678, 125, 890, 560, 340, 720, 910, 300, 640, 150, 275, 800, 455]

    # Main program loop
    while True:
        print("Sorting Algorithms Menu")
        print("Select a sorting operation (1-4):")
        print("1. Bubble Sort - Sort Student Names")
        print("2. Insertion Sort - Sort Test Scores")
        print("3. Quick Sort - Sort Book Prices")
        print("4. Exit program")

        choice = input("Enter your choice: ")


        if choice == '1':
            print(f"\nOriginal names: {student_names}")
            print("Performing Bubble sort...")
            sorted_names = insertion_sort(test_scores)
            print(f"Sorted scores: {sorted_names}")

        elif choice == '2':
            print(f"\nOriginal scores: {test_scores}")
            print("Performing Insertion Sort...")
            sorted_scores = insertion_sort(test_scores)
            print(f"Sorted scores: {sorted_scores}")

            top_5 = sorted_scores[-5:][::-1]  # take last 5 and reverse
            print("\nTop 5 Scores:")
            for i, score in enumerate(top_5, start=1):
                print(f"{i}. {score}")

        elif choice == '3':
            print(f"\nOriginal prices: {book_prices}")
            print("performing quick sort...")
            sorted_prices, recursive_calls = quick_sort(book_prices)
            print(f"Sorted prices: {sorted_prices}")
            print(f"Recursive calls: {recursive_calls}")

        elif choice == '4':
            print("Thank you for using the program!")
            break


        else:
            print("Inavald choice! Please enter a number between 1 and 4.")

        again = input("\nwould you like to perform another sort? (y/n): ").lower()
        if again != 'y':
            print("Thank you for using the sorting program!")
            break
        


if __name__=="__main__":
    main()
