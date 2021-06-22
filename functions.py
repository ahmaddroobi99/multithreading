import time

database_value =1


def square_numbers():
    for i in range(100):
        i*i


def increase ():
    global database_value

    local_copy = database_value
    #processing
    local_copy+=3
    time.sleep(0.1)
    # print(local_copy)
    database_value = local_copy
    # print(database_value)




