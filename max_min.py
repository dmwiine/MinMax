def find_min_max(arg):
    arg.sort()
    result = []  # Initialise empty list to store the result

    biggest = arg[0]
    smallest = arg[len(arg) - 1]

    if biggest == smallest:     # Checking to see if the numbers are the same
        result.append(biggest)
        return result
    else:
        result.append(biggest)  
        result.append(smallest)
        return result

print(find_min_max([6, 4]))