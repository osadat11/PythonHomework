def format_to_json(data):
    for num in range(len(data)):
        data_keys = data[num].keys()
        for num_i in range(len(data_keys)):
            print(data[num].data_keys[num_i])
            print(" , ")
        else:
            data_keys = []
            print("\n")
    return