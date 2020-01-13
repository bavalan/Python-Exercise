def function_names(name):
    '''
     (io.TextIOWrapper) -> list of str

     Will take in the name of a file,open it and read it.
     It wil then return the function names in that file.

     REQ: File needs to be in PEP8 format
    '''
    # Open the file and read it
    file = open(name, "r")
    # Open the file and read every line
    file = file.readlines()
    # Create a list
    word = []
    # For every line in the file
    for lines in file:
        # If the word "def" in the lines
        if("def" in lines):
            # Start the word after finding "def "
            first = (lines.index("def") + 4)
            # End the word before "(" comes up
            last = (lines.index("("))
            # Show the word between "def" and the first "(" in that line
            word.append(lines[first:last])
    # Return  the word
    return word


def justified(file):
    '''
    (io.TextIOWrapper) -> bool

    Will take in a  file,open it and read it.
    It wil then return False if at least one line of the file
    begins with A space.Else wise it wil return True if it does not

    REQ: File needs to be in PEP8 format
    '''
    # Open the file and read it
    File_Open = open(file, "r")
    # Open the file and read every line
    File_Open = File_Open.readlines()
    # For every line the reult is True
    result = True
    # For every line in the file
    for lines in File_Open:
        # If a line starts A SPACE
        if((lines.startswith(" ")) or (lines.startswith("\t"))):
            # The result is false
            result = False
    # Return the result
    return result