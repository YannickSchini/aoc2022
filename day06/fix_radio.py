PACKET_LENGTH = 4
MESSAGE_LENGTH = 14

def find_token_beginning(datastream_buffer: str, token_length: int) -> int:
    for i in range(len(datastream_buffer) - token_length):
        if len(set(datastream_buffer[i:i + token_length])) == token_length:
            return i + token_length

if __name__ == "__main__":
    filename = "input.txt"
    # filename = "test_1.txt" # Answer should be 7 for Part 1, 19 for Part 2
    # filename = "test_2.txt" # Answer should be 5 for Part 1, 23 for Part 2
    # filename = "test_3.txt" # Answer should be 6 for Part 1, 23 for Part 2
    # filename = "test_4.txt" # Answer should be 10 for Part 1, 29 for Part 2
    # filename = "test_5.txt" # Answer should be 11 for Part 1, 26 for Part 2
    with open(filename) as f:
        datastream_buffer = f.read().strip()
    print(find_token_beginning(datastream_buffer, PACKET_LENGTH))
    print(find_token_beginning(datastream_buffer, MESSAGE_LENGTH))
