
def top_n(items,n):
    """ This is a function that returns the top number of n in an array in descending order

    ARGS:
        items (array): list or array like object
        n (int): num of items to return

    Return: 
        returns an array: top n items in desc order

    Examples:
        >>> top_n([8,3,5,9,7,4],4)
            [9,8,7,5]
    """

    for i in range(n):  # Keep sorting until we have the top n items
        for j in range(len(items)-1-i):

            if items[j] > items[j+1]:  # If this item is bigger than next the item..
                items[j], items[j+1] = items[j+1], items[j]  # swap the two!

    # Get last two items
    top_n = items[-n:]

    # Return in descending order
    return top_n[::-1]