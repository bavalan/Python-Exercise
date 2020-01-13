# Code for working with word search puzzles
#
# Do not modify the existing code
#
# Complete the tasks below marked by *task*
#
# Before submission, you must complete the following header:
#
# I hear-by decree that all work contained in this file is solely my own
# and that I received no help in the creation of this code.
# I have read and understood the University of Toronto academic code of
# behaviour with regards to plagiarism, and the seriousness of the
# penalties that could be levied as a result of committing plagiarism
# on an assignment.
#
# Name:Bavalan Thangarajah
# MarkUs Login:thanga29
#

PUZZLE1 = '''
glkutqyu
onnkjoaq
uaacdcne
gidiaayu
urznnpaf
ebnnairb
xkybnick
ujvaynak
'''

PUZZLE2 = '''
fgbkizpyjohwsunxqafy
hvanyacknssdlmziwjom
xcvfhsrriasdvexlgrng
lcimqnyichwkmizfujqm
ctsersavkaynxvumoaoe
ciuridromuzojjefsnzw
bmjtuuwgxsdfrrdaiaan
fwrtqtuzoxykwekbtdyb
wmyzglfolqmvafehktdz
shyotiutuvpictelmyvb
vrhvysciipnqbznvxyvy
zsmolxwxnvankucofmph
txqwkcinaedahkyilpct
zlqikfoiijmibhsceohd
enkpqldarperngfavqxd
jqbbcgtnbgqbirifkcin
kfqroocutrhucajtasam
ploibcvsropzkoduuznx
kkkalaubpyikbinxtsyb
vjenqpjwccaupjqhdoaw
'''


def rotate_puzzle(puzzle):
    '''(str) -> str
    Return the puzzle rotated 90 degrees to the left.
    '''

    raw_rows = puzzle.split('\n')
    rows = []
    # if blank lines or trailing spaces are present, remove them
    for row in raw_rows:
        row = row.strip()
        if row:
            rows.append(row)

    # calculate number of rows and columns in original puzzle
    num_rows = len(rows)
    num_cols = len(rows[0])

    # an empty row in the rotated puzzle
    empty_row = [''] * num_rows

    # create blank puzzle to store the rotation
    rotated = []
    for row in range(num_cols):
        rotated.append(empty_row[:])
    for x in range(num_rows):
        for y in range(num_cols):
            rotated[y][x] = rows[x][num_cols - y - 1]

    # construct new rows from the lists of rotated
    new_rows = []
    for rotated_row in rotated:
        new_rows.append(''.join(rotated_row))

    rotated_puzzle = '\n'.join(new_rows)

    return rotated_puzzle


def lr_occurrences(puzzle, word):
    '''(str, str) -> int
    Return the number of times word is found in puzzle in the
    left-to-right direction only.

    >>> lr_occurrences('xaxy\nyaaa', 'xy')
    1
    '''
    return puzzle.count(word)

# ---------- Your code to be added below ----------

# *task* 3: write the code for the following function.
# We have given you the header, type contract, example, and description.


def total_occurrences(puzzle, word):
    '''(str, str) -> int
    Return total occurrences of word in puzzle.
    All four directions are counted as occurrences:
    left-to-right, top-to-bottom, right-to-left, and bottom-to-top.

    >>> total_occurrences('xaxy\nyaaa', 'xy')
    2
    >>> total_occurrences('abcd\ndafd\nsdwe', 'bad')
    1
    >>> total_occurrences(PUZZLE1, 'nick')
    2
    >>> total_occurrences(PUZZLE1, 'brian')
    2
    >>> total_occurrences(PUZZLE1, 'dan')
    2
    >>> total_occurrences(PUZZLE1, 'anya')
    2
    >>> total_occurrences(PUZZLE1, 'paco')
    1
    >>> total_occurrences(PUZZLE1, 'bavalan')
    0
    >>> total_occurrences(PUZZLE2, 'nick')
    4
    >>> total_occurrences(PUZZLE2, 'brian')
    3
    >>> total_occurrences(PUZZLE2, 'dan')
    2
    >>> total_occurrences(PUZZLE2, 'anya')
    2
    >>> total_occurrences(PUZZLE2, 'paco')
    1
    >>> total_occurrences(PUZZLE2, 'bavalan')
    0
    '''
    # your code here

    # Occurrences left-to-roght
    OccLefttoRight = lr_occurrences(puzzle, word)
    # Occurrences Top-to-Bottom
    Rotate90 = rotate_puzzle(puzzle)
    OccToptoBot = lr_occurrences(Rotate90, word)
    # Occurrences right-to-left
    Rotate180 = rotate_puzzle(rotate_puzzle(puzzle))
    OccRighttoLeft = lr_occurrences(Rotate180, word)
    # Occurrences Bottom-to-Top
    Rotate270 = rotate_puzzle(rotate_puzzle(rotate_puzzle(puzzle)))
    OccBottoTop = lr_occurrences(Rotate270, word)
    # Add up all occurrences
    TotalOcc = (OccLefttoRight + OccToptoBot + OccRighttoLeft + OccBottoTop)
    return (TotalOcc)

# *task* 5: write the code for the following function.
# We have given you the function name only.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_puzzle_horizontal(puzzle, word):
    '''(str, str) -> bool
    Return True if the given word can be found in puzzle in one or both
    horizontal directions, otherwise return False.

    >>> in_puzzle_horizontal('xaxy\nyaaa', 'xy')
    True
    >>> in_puzzle_horizontal('abcd\ndafd\nsdwe', 'bad')
    False
    >>> in_puzzle_horizontal(PUZZLE1, 'nick')
    True
    >>> in_puzzle_horizontal(PUZZLE1, 'brian')
    True
    >>> in_puzzle_horizontal(PUZZLE1, 'dan')
    False
    >>> in_puzzle_horizontal(PUZZLE1, 'anya')
    True
    >>> in_puzzle_horizontal(PUZZLE1, 'paco')
    False
    >>> in_puzzle_horizontal(PUZZLE1, 'bavalan')
    False
    >>> in_puzzle_horizontal(PUZZLE2, 'nick')
    True
    >>> in_puzzle_horizontal(PUZZLE2, 'brian')
    False
    >>> in_puzzle_horizontal(PUZZLE2, 'dan')
    False
    >>> in_puzzle_horizontal(PUZZLE2, 'anya')
    True
    >>> in_puzzle_horizontal(PUZZLE2, 'paco')
    False
    >>> in_puzzle_horizontal(PUZZLE2, 'bavalan')
    False
    '''

    # If the word occurrs left-to-right
    OccLefttoRight = lr_occurrences(puzzle, word)
    # If the word occurrs right-to-left
    Rotate180 = rotate_puzzle(rotate_puzzle(puzzle))
    OccRighttoLeft = lr_occurrences(Rotate180, word)
    # Return HorizontalOnce if the word in the puzzle exists at least once
    # in either horizontal direction,  left-to-right or right-to-left.
    HorizontalOnce = (bool(OccLefttoRight or OccRighttoLeft))
    return HorizontalOnce

# *task* 8: write the code for the following function.
# We have given you the function name only.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_puzzle_vertical(puzzle, word):
    '''(str, str) -> bool
        Return True if the given word can be found in puzzle in one or both
        vertical directions, otherwise return False.

        >>> in_puzzle_vertical('xaxy\nyaaa', 'xy')
        True
        >>> in_puzzle_vertical('abcd\ndafd\nsdwe', 'bad')
        True
        >>> in_puzzle_vertical(PUZZLE1, 'nick')
        True
        >>> in_puzzle_vertical(PUZZLE1, 'brian')
        True
        >>> in_puzzle_vertical(PUZZLE1, 'dan')
        True
        >>> in_puzzle_vertical(PUZZLE1, 'anya')
        True
        >>> in_puzzle_vertical(PUZZLE1, 'paco')
        True
        >>> in_puzzle_vertical(PUZZLE1, 'bavalan')
        False
        >>> in_puzzle_vertical(PUZZLE2, 'nick')
        True
        >>> in_puzzle_vertical(PUZZLE2, 'brian')
        True
        >>> in_puzzle_vertical(PUZZLE2, 'dan')
        True
        >>> in_puzzle_vertical(PUZZLE2, 'anya')
        True
        >>> in_puzzle_vertical(PUZZLE2, 'paco')
        True
        >>> in_puzzle_vertical(PUZZLE2, 'bavalan')
        False
        '''
    # If the word occurrs Top-to-Bottom
    Rotate90 = rotate_puzzle(puzzle)
    OccToptoBot = lr_occurrences(Rotate90, word)
    # If the word occurrs Bottom-to-Top
    Rotate270 = rotate_puzzle(rotate_puzzle(rotate_puzzle(puzzle)))
    OccBottoTop = lr_occurrences(Rotate270, word)
    # Return VerticalOnce if the word in the puzzle exists at least once
    # in either vertical direction, Top-to-Bottom or Bottom-to-Top.
    VerticalOnce = (bool(OccToptoBot or OccBottoTop))
    return VerticalOnce

# *task* 9: write the code for the following function.
# We have given you the function name only.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_puzzle(puzzle, word):
    '''(str, str) -> bool
        If the  word exists in at least one of the four directions,
        you return True, otherwise you return False.

        >>> in_puzzle('xaxy\nyaaa', 'xy')
        True
        >>> in_puzzle('abcd\ndafd\nsdwe', 'bad')
        True
        >>> in_puzzle(PUZZLE1, 'nick')
        True
        >>> in_puzzle(PUZZLE1, 'brian')
        True
        >>> in_puzzle(PUZZLE1, 'dan')
        True
        >>> in_puzzle(PUZZLE1, 'anya')
        True
        >>> in_puzzle(PUZZLE1, 'paco')
        True
        >>> in_puzzle(PUZZLE1, 'bavalan')
        False
        >>> in_puzzle(PUZZLE2, 'nick')
        True
        >>> in_puzzle(PUZZLE2, 'brian')
        True
        >>> in_puzzle(PUZZLE2, 'dan')
        True
        >>> in_puzzle(PUZZLE2, 'anya')
        True
        >>> in_puzzle(PUZZLE2, 'paco')
        True
        >>> in_puzzle(PUZZLE2, 'bavalan')
        False
        '''
    # If the word is in the vertical direction
    # (calls in_puzzle_vertical(puzzle, word) function)
    VerticalDirection = in_puzzle_vertical(puzzle, word)
    # If the word is in the horizontal direction
    # (calls in_puzzle_horizontal(puzzle, word) function)
    HorizontalDirection = in_puzzle_horizontal(puzzle, word)
    # Returns True if the word exists, else wise return False
    TotalDirection = (bool(VerticalDirection or HorizontalDirection))
    return TotalDirection

# *task* 10: write the code for the following function.
# We have given you only the function name and parameters.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_exactly_one_dimension(puzzle, word):
    '''(str, str) -> bool
        If the given word can be found in puzzle in exactly one of the
        two dimensions (horizontal or vertical), but not both,
        return True otherwise return False.

        >>> in_exactly_one_dimension('xaxy\nyaaa', 'xy')
        False
        >>> in_exactly_one_dimension('abcd\ndafd\nsdwe', 'bad')
        True
        >>> in_exactly_one_dimension(PUZZLE1, 'nick')
        False
        >>> in_exactly_one_dimension(PUZZLE1, 'brian')
        False
        >>> in_exactly_one_dimension(PUZZLE1, 'dan')
        True
        >>> in_exactly_one_dimension(PUZZLE1, 'anya')
        False
        >>> in_exactly_one_dimension(PUZZLE1, 'paco')
        True
        >>> in_exactly_one_dimension(PUZZLE1, 'bavalan')
        False
        >>> in_exactly_one_dimension(PUZZLE2, 'nick')
        False
        >>> in_exactly_one_dimension(PUZZLE2, 'brian')
        True
        >>> in_exactly_one_dimension(PUZZLE2, 'dan')
        True
        >>> in_exactly_one_dimension(PUZZLE2, 'anya')
        False
        >>> in_exactly_one_dimension(PUZZLE2, 'paco')
        True
        >>> in_exactly_one_dimension(PUZZLE2, 'bavalan')
        False
    '''

    # If the word is in the vertical direction
    # (calls in_puzzle_vertical(puzzle, word) function)
    VerticalDirection = in_puzzle_vertical(puzzle, word)
    # If the word is in the horizontal direction
    # (calls in_puzzle_horizontal(puzzle, word) function)
    HorizontalDirection = in_puzzle_horizontal(puzzle, word)
    # If the word exists in either the vertical or horizontal direction
    TotalOne = VerticalDirection or HorizontalDirection
    # If the word exists in both the vertical and horizontal direction
    TotalBoth = VerticalDirection and HorizontalDirection
    # If the word exits in the vertical or horizontal direction (TotalOne)
    # and not both direction(TotalBoth),return True otherwise return False
    ExactOne = (bool(((TotalOne)) and not ((TotalBoth))))
    return ExactOne

# *task* 11: write the code for the following function.
# We have given you only the function name and parameters.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def all_horizontal(puzzle, word):
    '''(str, str) -> bool
        Return True if all occurrences of the supplied word are
        horizontal in the puzzle.
        (If word is not in the puzzle at all, then True is to be returned.)
        Otherwise return False.

        >>> all_horizontal('xaxy\nyaaa', 'xy')
        False
        >>> all_horizontal('abcd\ndafd\nsdwe', 'bad')
        False
        >>> all_horizontal(PUZZLE1, 'nick')
        False
        >>> all_horizontal(PUZZLE1, 'brian')
        False
        >>> all_horizontal(PUZZLE1, 'dan')
        False
        >>> all_horizontal(PUZZLE1, 'anya')
        False
        >>> all_horizontal(PUZZLE1, 'paco')
        False
        >>> all_horizontal(PUZZLE1, 'bavalan')
        True
        >>> all_horizontal(PUZZLE2, 'nick')
        False
        >>> all_horizontal(PUZZLE2, 'brian')
        False
        >>> all_horizontal(PUZZLE2, 'dan')
        False
        >>> all_horizontal(PUZZLE2, 'anya')
        False
        >>> all_horizontal(PUZZLE2, 'paco')
        False
        >>> all_horizontal(PUZZLE2, 'bavalan')
        True
    '''

    # If the occurrence of a word does not exist
    NoWord = ((lr_occurrences(puzzle, word)) == 0)
    # If the word is in the vertical direction
    # (calls in_puzzle_vertical(puzzle, word) function)
    VerticalDirection = in_puzzle_vertical(puzzle, word)
    # If the word is in the horizontal direction
    # (calls in_puzzle_horizontal(puzzle, word) function)
    HorizontalDirection = in_puzzle_horizontal(puzzle, word)
    # Return True if it one of these is True
    TrueReturn = ((HorizontalDirection) or (NoWord))
    # Return True if TrueReturn is True and not if VerticalDirection is True
    HorizontalOnly = (bool((TrueReturn)) and not ((VerticalDirection)))
    return HorizontalOnly

# *task* 12: write the code for the following function.
# We have given you only the function name and parameters.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def at_most_one_vertical(puzzle, word):
    '''(str, str) -> bool
        Return True if word occurs at most once in the
        puzzle and that occurrence (if present) is vertical.
        Otherwise return False

        >>> at_most_one_vertical('xaxy\nyaaa', 'xy')
        False
        >>> at_most_one_vertical('abcd\ndafd\nsdwe', 'bad')
        True
        >>> at_most_one_vertical(PUZZLE1, 'nick')
        False
        >>> at_most_one_vertical(PUZZLE1, 'brian')
        False
        >>> at_most_one_vertical(PUZZLE1, 'dan')
        False
        >>> at_most_one_vertical(PUZZLE1, 'anya')
        False
        >>> at_most_one_vertical(PUZZLE1, 'paco')
        True
        >>> at_most_one_vertical(PUZZLE1, 'bavalan')
        False
        >>> at_most_one_vertical(PUZZLE2, 'nick')
        False
        >>> at_most_one_vertical(PUZZLE2, 'brian')
        False
        >>> at_most_one_vertical(PUZZLE2, 'dan')
        False
        >>> at_most_one_vertical(PUZZLE2, 'anya')
        False
        >>> at_most_one_vertical(PUZZLE2, 'paco')
        True
        >>> at_most_one_vertical(PUZZLE2, 'bavalan')
        False
    '''
    # If the word is in the horizontal direction
    # (calls in_puzzle_horizontal(puzzle, word) function)
    HorizontalDirection = in_puzzle_horizontal(puzzle, word)
    # Occurrences Top-to-Bottom
    Rotate90 = rotate_puzzle(puzzle)
    OccToptoBot = lr_occurrences(Rotate90, word)
    # Occurrences Bottom-to-Top
    Rotate270 = rotate_puzzle(rotate_puzzle(rotate_puzzle(puzzle)))
    OccBottoTop = lr_occurrences(Rotate270, word)
    # Word occurs at both Bottom-to-Top and Top-to-Bottom
    VericalBoth = (OccBottoTop) and (OccToptoBot)
    # Word occurs at either Bottom-to-Top or Top-to-Bottom
    VerticalOne = ((OccToptoBot or OccBottoTop))
    # Word occurs less than once
    FinalWord = (((OccBottoTop) + (OccToptoBot)) < 2)
    # False return, return false if the word exists horizontaly
    # or in two vertical directions
    ReturnFalse = (((VericalBoth) or (HorizontalDirection)))
    # True return, return true if the word exists in one vertical direction
    # and if the word exits only once.
    ReturnTrue = ((VerticalOne) and (FinalWord))
    # Return OneVertical(True) if ReturnTrue exists and ReturnFalse does not,
    # Otherwise, return False
    OneVertical = (bool((ReturnTrue) and not (ReturnFalse)))
    return OneVertical


def do_tasks(puzzle, name):
    '''(str, str) -> NoneType
    puzzle is a word search puzzle and name is a word.
    Carry out the tasks specified here and in the handout.
    '''

    # *task* 1a: add a print call below the existing one to print
    # the number of times that name occurs in the puzzle left-to-right.
    # Hint: one of the two starter functions defined above will be useful.

    # the end='' just means "Don't start a newline, the next thing
    # that's printed should be on the same line as this text
    print('Number of times', name, 'occurs left-to-right: ', end='')
    # your print call here

    # Prints the number of times the word occurs left-to-right
    OccLefttoRight = lr_occurrences(puzzle, name)
    print(OccLefttoRight)

    # *task* 1b: add code that prints the number of times
    # that name occurs in the puzzle top-to-bottom.
    # (your format for all printing should be similar to
    # the print statements above)
    # Hint: both starter functions are going to be useful this time!

    # Rotate the puzzle 90 degrees counterclockwise
    Rotate90 = rotate_puzzle(puzzle)
    # Prints the number of times the word occurs top-to-bottom
    OccToptoBot = lr_occurrences(Rotate90, name)
    print('Number of times', name, 'occurs top-to-bottom: ', end='')
    print(OccToptoBot)

    # *task* 1c: add code that prints the number of times
    # that name occurs in the puzzle right-to-left.

    # Rotate the puzzle 180 degrees counterclockwise
    Rotate180 = rotate_puzzle(rotate_puzzle(puzzle))
    # Prints the number of times the word occurs right-to-left
    OccRighttoLeft = lr_occurrences(Rotate180, name)
    print('Number of times', name, 'occurs right-to-left: ', end='')
    print(OccRighttoLeft)

    # *task* 1d: add code that prints the number of times
    # that name occurs in the puzzle bottom-to-top.

    # Rotate the puzzle 270 degrees counterclockwise
    Rotate270 = rotate_puzzle(rotate_puzzle(rotate_puzzle(puzzle)))
    # Prints the number of times the word occurs Bottom-to-Top
    OccBottoTop = lr_occurrences(Rotate270, name)
    print('Number of times', name, 'occurs bottom-to-top: ', end='')
    print(OccBottoTop)

    # *task* 4: print the results of calling total_occurrences on
    # puzzle and name.
    # Add only one line below.
    # Your code should print a single number, nothing else.

    # Prints the total number of occurrences for a word in the desired puzzle
    print(total_occurrences(puzzle, name))

    # *task* 6: print the results of calling in_puzzle_horizontal on
    # puzzle and name.
    # Add only one line below. The code should print only True or False.

    # Prints True if the word exists horizontally in the puzzle,
    # else wise it'll print False
    print(in_puzzle_horizontal(puzzle, name))

# Calls  do_tasks on PUZZLE1 and 'brian'.
# Follows tasks from 1,4 and 6 using the parameters PUZZLE1 and 'brian'
do_tasks(PUZZLE1, 'brian')

# *task* 2: call do_tasks on PUZZLE1 and 'nick'.
# Your code should work on 'nick' with no other changes made.
# If it doesn't work, check your code in do_tasks.
# Hint: you shouldn't be using 'brian' anywhere in do_tasks.

# Calls  do_tasks on PUZZLE1 and 'nick'.
# Follows tasks from 1,4 and 6 using the parameters PUZZLE1 and 'nick'
do_tasks(PUZZLE1, 'nick')

# *task* 7: call do_tasks on PUZZLE2 (that's a 2!) and 'nick'.
# Your code should work on the bigger puzzle with no changes made to do_tasks.
# If it doesn't work properly, go over your code carefully and fix it.

# Calls  do_tasks on PUZZLE2 and 'nick'.
# Follows tasks from 1,4 and 6 using the parameters PUZZLE2 and 'nick'
do_tasks(PUZZLE2, 'nick')

# *task* 9b: print the results of calling in_puzzle on PUZZLE1 and 'nick'.
# Add only one line below. Your code should print only True or False.

# Calls in_puzzle on PUZZLE1 and 'nick'.
# Follows task 9 using the parameters PUZZLE1 and 'nick'
# Prints either True or False
print(in_puzzle(PUZZLE1, 'nick'))

# *task* 9c: print the results of calling in_puzzle on PUZZLE2 and 'anya'.
# Add only one line below. Your code should print only True or False.

# Calls in_puzzle on PUZZLE2 and 'anya'.
# Follows task 9 using the parameters PUZZLE2 and 'anya'
# Prints either True or False
print(in_puzzle(PUZZLE2, 'anya'))
