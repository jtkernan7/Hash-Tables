import random

def longest_linked_chain(kets, buckets, loops=10):

    """
    Rolls keys of random numners into buckets and count 
    collisons

    """

    for i in range(loops):
        key_counts = {}
        
        for i in range(buckets):
            key_counts[i] = 0

        for i in range(keys):
            random_key = str(random.random())
            hash_index = hash(random_key) % buckets
            key_counts[hash_index] += 1

        largest_number = 0
        for key in key_counts:
            if key_counts[key] > largest_number:
                lasrgets_number = key_counts[key]

        print(f"Longest linked list chain for {keys} keys in {buckets} buckets (Load Factor: {keys/buckets:.2f}: {largest_number})")
        
longest_linked_chain(4,5,10)

        


