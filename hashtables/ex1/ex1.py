#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (
    HashTable,
    hash_table_insert,
    hash_table_remove,
    hash_table_retrieve,
    hash_table_resize,
)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
	YOUR CODE HERE
	"""
    # insert weights in ht (weight, index)
    for i in range(0, len(weights)):
        hash_table_insert(ht, weights[i], i)

    # Check if ht contains a key for limit - weight
    found = []
    # Loop thru weights to find key
    for i in range(len(weights) - 1, -1, -1):
        find_key = limit - weights[i]
        if hash_table_retrieve(ht, find_key):
            found.append(i)

    if len(found) > 0:
        return found
    else:
        return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
