#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (
    HashTable,
    hash_table_insert,
    hash_table_remove,
    hash_table_retrieve,
    hash_table_resize,
)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
	YOUR CODE HERE
	"""

    # tickets is an array of Tickets
    # tickets = [Ticket, Ticket, Ticket]

    # Loop thru tickets to insert tickets to hashtable
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # start at first ticket where none  is the source
    destination = "NONE"
    # print("First", first)

    for i in range(0, length):
        destination = hash_table_retrieve(hashtable, destination)
        route[i] = destination

    print(route)
    # Return route minus the last one
    return route[:-1]
