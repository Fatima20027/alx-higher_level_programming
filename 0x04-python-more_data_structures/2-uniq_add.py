def uniq_add(my_list=[]):
    uniq_add = set(my_list)
    for i in my_list:
        if i not in uniq_add:
            uniq_add.add(i)
    return sum(uniq_add)
