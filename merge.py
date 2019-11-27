# A function for merging multiple lists into one
#
# Parameter
#   ls - A list of lists where each inner element is a list to be merged into the master list
# Returns
#   A single list containing all unique elements from each list


def merge_lists(ls):
    master_filter_set = set()
    for l in ls:
        for el in l:
            master_filter_set.add(el)
    return list(master_filter_set)
