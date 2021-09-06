import random
def create_list(n):
    my_list = []
    for i in range(n):
        my_list.append(random.randint(1,6))
    return my_list

my_list = create_list(5)
print(my_list)



