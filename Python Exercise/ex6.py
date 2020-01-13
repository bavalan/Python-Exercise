def copy_me(List):
    '''
    (list)->list

    Function takes a list as the parameter,
    and returns a copy of the list with the following
    changes:
    • Strings have all their letters converted to upper-case
    • Integers and floats have their value increased by 1
    • booleans are negated (False becomes True, True becomes False)
    • Lists are replaced with the word ”List”
    Not a mutation

    REQ: len(List) > 0

    >>>copy_me([1,2.5,"HeLlo",True,False,[1,2,45,"Hi"]])
    [2,3.5,"HELLO",False,True,"List"]

    '''
    # Variable for the copy List
    NewList = []
    # Variable for the boolean logics
    true = True
    false = False

    # For every character in the list
    for characters in List:

        # If the character is a string
        if(type(characters) == str):
            # All character will be upper case
            characters = characters.upper()
            # These new changes will be added to the new list
            NewList.append(characters)

        # If the character is an interger
        elif(type(characters) == int):
            # All intergers will be increased bt 1
            characters = (characters + 1)
            # These new changes will be added to the new list
            NewList.append(characters)

        # If the character is a float
        elif(type(characters) == float):
            # All floats will be increased bt 1
            characters = (characters + 1)
            # These new changes will be added to the new list
            NewList.append(characters)

        # If the character is a bool
        elif(type(characters) == bool):
            # If the character is a True
            if(characters == true):
                # It will become False
                characters = false
                # These new changes will be added to the new list
                NewList.append(characters)

            # If the character is a False
            elif(characters == false):
                # It will become True
                characters = true
                # These new changes will be added to the new list
                NewList.append(characters)

        # If the character is a list
        elif(type(characters) == list):
            characters = "List"
            # These new changes will be added to the new list
            NewList.append(characters)

        # If its anything else
        else:
            # These new changes will be added to the new list
            NewList.append(characters)

    # Return the copy of the NewList
    return NewList


def mutate_me(List):
    '''
    (list)->NoneType

    Function takes lists as a parameter and returns None, and changes the
    input list in the following ways:
    • Strings have all their letters converted to upper-case
    • Integers and floats have their value increased by 1
    • booleans are negated (False becomes True, True becomes False)
    • Lists are replaced with the word ”List”
    This does not return a copy of the list but instead changes the parameter
    entered itself.

    REQ: len(List) > 0

    >>>mutate_me([1,2.5,"HeLlo",True,False,[1,2,45,"Hi"]])

    '''

    # A counter value set to 0 index value
    Counter = 0
    true = True
    false = False

    # While the length of the list is greater than 0 index value
    while(Counter < len(List)):

        # The Counterth character will always be the Counterth character
        List[Counter] = List[Counter]

        # If the character is a string and is in any of the indexes
        if(type(List[Counter]) == str):
            # Then at that index value in the List will be Uppercase
            List[Counter] = List[Counter].upper()

        # If the character is a interger and is in any of the indexes
        elif(type(List[Counter]) == int):
            # Then at that index value in the List will be increased by 1
            List[Counter] = (List[Counter] + 1)

        # If the character is a float and is in any of the indexes
        elif(type(List[Counter]) == float):
            # Then at that index value in the List will be increased by 1
            List[Counter] = (List[Counter] + 1)

        # If the character is a bool and is in any of the indexes
        elif(type(List[Counter]) == bool):
            # If the value at that index is True
            if(List[Counter] == true):
                # Then the value at that index wil be False
                List[Counter] = false

            # If the value at that index is False
            elif(List[Counter] == false):
                # Then the value at that index wil be True
                List[Counter] = true

        # If the character is a list and is in any of the indexes
        elif(type(List[Counter]) == list):
            List[Counter] = 'List'

        # If its anything else
        else:
            List[Counter] = List[Counter]

        # Continue to add 1 to find out what type the next index will be
        Counter += 1
