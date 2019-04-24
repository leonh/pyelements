import inspect  # import from the 'standard library'

# #### Code blocks
# significant whitespace indentation ! typical 4 spaces


# a function
def line() -> str:
    # return False
    return "line %s:" % inspect.currentframe().f_back.f_lineno


# code block with 3 indent levels
def open_a_file(filepath):
    with open(file=filepath) as f:
        for text_line in f.readlines():
            print(line(), text_line)
            #print(text_line, end='')


# compound statements indented with 4 spaces
# __name__ is a built-in variable which evaluates
# to the name of the current module.
# if your module is the entry point of code execution
# then __name__ is set to "__main__"

if __name__ == "__main__":  # common python idiom
    print(line(), globals())
    open_a_file(filepath='test.txt')

