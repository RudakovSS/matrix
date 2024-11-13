def apply_all_func(int_list, *functions):
    results = {}

    for func in functions:
        results[func.__name__] = func(int_list)
    return results

numbers = [1, 4, 7, 6, 88, 34]
results = apply_all_func(numbers, min, max, len, sum, sorted)
print(results)