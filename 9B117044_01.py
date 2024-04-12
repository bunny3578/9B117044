def get_even_squares(num_list):
    even_squares = [num ** 2 for num in num_list if num % 2 == 0]
    return even_squares


def get_odd_cubes(num_list):
    odd_cubes = [num ** 3 for num in num_list if num % 2 != 0]
    return odd_cubes


def get_sliced_list(num_list):
    return num_list[4:]


def format_numbers(num_list):
    formatted_numbers = ['{:>8}'.format(num) for num in num_list]
    return formatted_numbers


num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_squares = get_even_squares(num_list)
odd_cubes = get_odd_cubes(num_list)
sliced_list = get_sliced_list(num_list)

print(", ".join(format_numbers(even_squares)))
print(", ".join(format_numbers(odd_cubes)))
print(", ".join(format_numbers(sliced_list)))

