def insert(List, ListCombine, Index):
    '''
    (list,list,int) -> list
    (str,str,int) -> str

    Takes in 3 parameters two of the same and an index, then returns a copy of
    the first parameter with the elements of the second parameter
    inserted at the given index of the first parameter.

    REQ: First two parameters must be the same
    and has to be either a list or string
    REQ: Index >= 0

    >>> insert([1, 2, 3], ['a', 'b', 'c'], 2)
    [1, 2, 'a', 'b', 'c', 3]
    >>> insert("123","abc",2)
    '12abc3'

    '''

    # If the first parameter is a string
    if (List == str(List)):
        # Add the elements of the second parameter after the index
        NewList = List[:Index] + ListCombine + List[Index:]
        return NewList
    # If the first parameter is a list
    else:
        NewList = List
        # Add the elements of the second parameter after the index
        NewList[Index:Index] = ListCombine
        return NewList


def up_to_first(List, Object):
    '''
    (list,object) -> list
    (str,object) -> str

    Takes two parameters, a list (or string) and an object, and returns
    a copy of the list up to (but not including) the first
    occurrence of that object, or all of the elements if that
    object is not in the list.

    REQ: First  parameters has to be either a list or string

    >>> up_to_first([1, 2, 3, 4], 3)
    [1, 2]
    >>> up_to_first([1, 2, 3, 4], 9)
    [1, 2, 3, 4]
    '''

    # If the object is in the first parameter
    if(Object in List):
        # Show all the elements in the first parameter until the index
        NewList = List[:List.index(Object)]
        return NewList
        # If the object is not in the first parameter
    else:
        # Return the first parameter
        return List


def cut_list(List, Index):
    '''
      (list,int) -> list
      (str,int) -> str

      Given a list and an index, returns a copy of the
      list, but with the items before and after the index swapped.

      REQ: First  parameter has to be either a list or string
      REQ: Second  parameter has to be an interger

      >>> cut_list([0,1,2,3,4,5,6,7,8,9], 3)
      [4, 5, 6, 7, 8, 9, 3, 0, 1, 2]
      >>> cut_list("ABCDEFGX1234",7)
      '1234XABCDEFG'
      '''

    # Return every value after the given index besides the index itself.
    # Then return the index and every value before the index
    NewList = List[Index + 1:] + List[Index:Index + 1] + List[:Index]
    return NewList
