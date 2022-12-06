def get_data():
    with open("Day 6\\input.txt", "r") as file:
        guide = file.readlines()
    return guide

def day_6_function(part: str="PartI"):
    data_stream = get_data()
    data_stream = data_stream[0].strip()
    
    for i in range(len(data_stream)):
        if part == "PartI":
            start_set = set(data_stream[i:i+4])
            if len(start_set) == 4:
                return i+4
        else:
            start_set = set(data_stream[i:i+14])
            if len(start_set) == 14:
                return i+14

if __name__ == "__main__":
    packet_marker = day_6_function()
    message_marker = day_6_function(part="PartII")

    print(packet_marker)
    print(message_marker)

