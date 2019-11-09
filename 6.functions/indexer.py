from reverse import reverse


def get(collection, idx_key):
    """Return element from collection by index or key.

    Parameters
    ----------
    collection : list, tuple, dict or str.
        Almost any type of collection.
    idx_key : hashable element, I guess
        Index or key of element in collection.

    Returns
    -------
    element : whatever
        Element with given index or key.
    """
    if not isinstance(collection, dict):
        if idx_key >= 0:
            count = 0
            for i in collection:
                if count == idx_key:
                    return i
                else:
                    count += 1
        else:
            count = -1
            for i in reverse(collection):
                if count == idx_key:
                    return i
                else:
                    count -= 1
    else:
        for key, value in collection.items():
            if key == idx_key:
                return value
    raise IndexError


if __name__ == '__main__':
    print(get([1, 2, 15, 36], 2))
    print(get((1, 2, 15, 36), -1))
    print(get({1: 2, 'kva': 36}, 'kva'))
