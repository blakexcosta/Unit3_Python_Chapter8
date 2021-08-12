def main():
    print("he;llo")
    # Chapter 8 lists

    # create new list
    numbers = [1, 2, 3, 4, 5]
    strings = ["bob", "billy", "suzie"]
    mixed_data = ["bob", 45, 6]

    # eleements start at zero
    print(mixed_data[1])

    # List length
    print(len(mixed_data))

    # in and not in
    print("Blake" in strings)
    print("bob" in strings)

    # list slicing
    # list slicing the end number (end index) is exclusive
    new_list = numbers[0:3]
    print(new_list)

    # lists ARE mutable
    new_list[0] = 22
    print(new_list)

    # delete/removing elements from list
    del new_list[0]
    # can also remove slices of list like del new_list[0:2]
    print(new_list)

    # inserting multiple new elements
    new_list = [2, 4, 6, 8, 20]
    new_list[4:4] = [10, 12, 14]
    print(new_list)

    # replacing multiple elemtns
    # remember again. the end index is always exclusive and start index is INCLUSIVE
    new_list[0:3] = ["replaced element1", "replaced element2"]
    print(new_list)

    # removing elements
    new_list[0:2] = []  # it looks ugly so removing strings from list
    print(new_list)

    # list methods
    # https://education.launchcode.org/lchs/chapters/lists/list-methods.html

    # iteratings throuhg lists
    for item in new_list:
        print(item)

    # common list tasks
    # switiching two elements
    new_list = ['m', 'a', 'c', 'h', 'o', 'c', 'a', 't']
    temp_val = new_list[0]
    new_list[0] = new_list[-1]
    new_list[-1] = temp_val
    print(new_list)

    # accumulating list elements to another list
    # incrementing by two in python range
    some_more_numbers = []
    for val in range(0, 42, 2):
        some_more_numbers.append(val)
    print(some_more_numbers)

    # easy way to find min and max
    new_list = [-21, -100, 3, 45, 69, 2, 21]
    new_list.sort()
    min = new_list[0]
    max = new_list[-1]
    print(f"\tmin value: {min}\n\tmax value:{max}")

    # making an independent copy of a list
    list_clone = new_list.copy()
    del list_clone[0]
    new_list[0] = 69
    print(list_clone, new_list)

    # spliting and joining lists
    text = "be the best around, no one gonna keep you down"
    individual_words = text.split(',')
    print(individual_words)

    # list conversion
    new_list = list("Bobs burgers")
    print(new_list)


if __name__ == "__main__":
    main()
