class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity                # number of slots in the hash table
        self.storage = [None] * capacity        # fills self.storage list with the same number of None's as we have capacity
        self.size = 0                           # counts all the nodes in the linked list


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


    def get_load_factor(self):                  # how full the table is
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.size / self.capacity

    # the following two methods are hashing functions -- we only need to use one of these

    def fnv1(self, key):                        
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        FNV_prime = 1099511628211
        FNV_offset = 14695981039346656037
        hash = FNV_offset

        for char in key:
            hash = hash * FNV_prime
            hash = hash ^ ord(char)             # ord() converts string to binary equivalent to an ASCII number

        return hash 


    # def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)
        node = HashTableEntry(key, value)               # created a new node
        if self.storage[index] is not None:            
            if self.storage[index].key == key:           # if the key is the one we want we are going to -->
                self.storage[index].value = value       # update the value
            else:
                current = self.storage[index]           # creating a new pointer
                while current.next is not None:         # while the next node of the current index is not none
                    if current.key == key:
                        current.value = value
                    else:
                        current = current.next
                if current.key == key:                  # this will check the very last node
                    current.value = value               # update the value
                else:                                   # if we never find the node we are looking for, we are going to add a new node
                    current.next = node
                    self.size += 1                      # self.size counts all the nodes
        else:
            self.storage[index] = node
            self.size += 1


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if self.storage[index] is None:                             # checking to see if they key does not exist in the table
            print("This key does not exist in the table.")
            return
        if self.storage[index].key == key:                          # if they very first key at the index is the one we are looking for
            if self.storage[index].next is not None:                # if there is something after self.storage at index -->
                self.storage[index] = self.storage[index].next      # reset pointer to equal the node that came after it, deleting the pointer
            else:
                self.storage[index] = None
        else:
            current = self.storage[index].next
            prev = self.storage[index]
            while current is not None:
                if current.key == key:
                    prev.next = current.next
                    self.size -= 1
                else:
                    prev = current
                    current = current.next


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if self.storage[index] is None:             # if there is no node at index of self.storage return None
            return None
        current = self.storage[index]               # create pointer 
        while current:
            if current.key == key:                  # if the current key is equal to the key passed in, return the value of the current 
                return current.value
            else:
                current = current.next              # if the key was not found move the pointer to the next node
        return None                                 # return None if the key was not found


    def resize(self, new_capacity):                 # this method will be used when we have filled all of our capacity and we need more space
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        self.capacity = new_capacity                
        old_storage = self.storage                  # store old storage in old_storage variable
        self.storage = [None] * self.capacity
        for node in old_storage:                    # goes through first node in every index
            if node is not None:                    
                self.put(node.key, node.value)      # add node into the list -- only move the head nodes because it's a linked list



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
