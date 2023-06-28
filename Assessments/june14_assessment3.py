def count_positive_negative(numbers):
    postive_count = 0
    negative_count = 0

    for num in numbers:
        if num > 0:
            postive_count += 1
        elif num < 0:
            negative_count += 1
    return postive_count, negative_count

counter = count_positive_negative([1,2,3,4,5,-6,-7,-8])
print(counter)