# Returns a list of strings, one per line. Empty lines will be 
# an empty string in the list
def get_list_of_strings(input_file_path, separation=None):
    with open(input_file_path) as input_file:
        input_file_lines = input_file.read()
    if separation is None:
        return input_file_lines.splitlines()
    return [group.splitlines() for group in input_file_lines.split(separation)]

# Must have tuples of the same length
def add_tuples(tuple_1, tuple_2):
    if len(tuple_1) != len(tuple_2):
        return None
    else:
        return tuple(map(lambda i, j: i + j, tuple_1, tuple_2))