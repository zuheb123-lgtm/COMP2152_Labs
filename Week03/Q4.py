#Question 4

monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana, "Eve", "Frank"}
monday_class.add("Grace")
print(f"Monday class: {monday_class}")
print(f"Monday class: {wednesday_class}")
print(f"Attended both class: {monday_class & wednesday_clas}")
print(f"Attended either class: {monday_class | wednesday_clas}") #  pipe sign = |
print(f"Only Monday: {monday_class - wednesday_clas}")
print(f"Only One class (not both): {monday_class ^ wednesday_clas}") # caret sign = ^
all_classes = monday_class | wednesday_clas
print(f"Is Monday subset of all students? :, "{monday_class <= all_classes})