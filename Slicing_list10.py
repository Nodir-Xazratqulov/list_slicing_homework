def main(list1,n):
    """
    A list of several elements is given. Return all elements in reverse order except n elements from the beginning.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    list2 = list1[::-1]
    return list2[0:n]
print(main(['a', 'b', 'c', 'd', 'e', 'f'],3))