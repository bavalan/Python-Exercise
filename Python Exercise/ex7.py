def create_dict(file):
    '''
    (io.TextIOWrapper) -> dict of {str: [str, str, str, int, str]}

    This function will read a file and, each line will have a
    username, first name, last name, age, gender (either M or F)
    and an e-mail address, all separated by a whitespace.
    The function will insert each person’s information into a dictionary with
    their username as the key, along with rest of the information. It will then
    return a dictionary:

    REQ:File must exist in the same place as the program.
    '''

    # Variable for the dictionary is created
    D = {}
    # Reads all the lines in the file
    Read = file.readlines()

    # Loop: For every line in the file
    for Lines in Read:

        # Splits, whenever a whitespace occurs in each line
        Info = Lines.split()

        # The key will be the username [0] and it will display everything
        # After the key[1] value
        Info[3] = int(Info[3])
        D[Info[0]] = Info[2:3] + Info[1:2] + Info[5:6] + Info[3:4] + Info[4:5]

    # Returns the new dictionary
    return D


def update_field(Dicts, User, Fields, Replace):
    '''

     (dict of {str: [str, str, str, int, str]}, str, str, int/str)
     -> dict of {str: [str, str, str, int, str]}

     Function takes 4 parameters: A dictionary in the format created by
     the previous function, a username, the name of a field
     (One of: ’LAST’, ’FIRST’, ’E-MAIL’, ’AGE’ or’GENDER’2),
     and a new value to replace the current value of the specified field

     REQ: A username must exist in the dictionaries

     >>> my_dict = {'sclause':['Clause','Santa','santa@christmas.np',450,'M']}
     >>> update_field(my_dict,'sclause','AGE',999)
     >>> my_dict == {'sclause':['Clause','Santa','santa@christmas.np',999,'M']}
     True
    '''

    # A list created containing each field in the appropriate spot
    FieldList = ['LAST', 'FIRST',  'E-MAIL', 'AGE', 'GENDER']

    # The Key is coppied to a new list
    Info = Dicts[User]

    # The neccessary field that needs to be replaced  at the index
    Info[FieldList.index(Fields)] = Replace

    # The new info is updated back to the key
    Dicts[User] = Info
