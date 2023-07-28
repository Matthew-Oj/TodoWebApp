FILEPATH = "todos.txt"


# go practice to hold constants like this caps on top of function


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    # doc-strings to explain what function does with help command
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Writes a to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


# do not need to return anything as it is a file modification


if __name__ == "__main__":
    print("Test from fun")
