#Question 2

cart = ["apple" , "banana", "milk", "bread", "apple", "eggs"]
apple_count = cart.count("apple")
print("Number of apples: ", apple_count)
milk_position = cart.index("milk")
print("Position of milk: ", milk_position)
removed_item = cart.remove("apple")
print("Removed Duplicate Apple: ", cart)
removed_item = cart.pop()
print("Removed item using pop: ", removed_item)
print(f"FInal Cart: , {cart}")