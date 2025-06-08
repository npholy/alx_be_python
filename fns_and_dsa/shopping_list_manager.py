def display_menu(): 
    print(f"Shopping List Manager") 
    print("1. Add Item") 
    print("2. Remove Item") 
    print("3. View List") 
    print("4. Exit") 
 
def main(): 
    shopping_list = [] 
    while True: 
        display_menu() 
        try: 
            choice = int(input("Enter your choice: "))  
        except ValueError: 
            print("Invalid input. Please enter a number.") 
            continue 
        if choice == 1: 
            item = input("Enter the item to add: ") 
            shopping_list.append(item) 
        elif choice == 2: 
            item = input("Enter the item to remove: ")
            if item in shopping_list: 
                shopping_list.remove(item) 
            else: 
                print("Item not found in list") 
        elif choice == 3: 
            print("Current Shopping List:") 
            for item in shopping_list: 
                print(f"- {item}") 
        elif choice == 4: 
            print("Goodbye!") 
            break 
        else: 
            print("Invalid choice. Enter 1-4.") 
 
if __name__ == "__main__": 
    main() 
