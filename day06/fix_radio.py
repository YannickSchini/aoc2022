from argparse import ArgumentParser, FileType

PACKET_LENGTH = 4
MESSAGE_LENGTH = 14

def find_token_end(datastream_buffer: str, token_length: int) -> int:
    for i in range(len(datastream_buffer) - token_length):
        if len(set(datastream_buffer[i:i + token_length])) == token_length:
            return i + token_length

if __name__ == "__main__":
    parser = ArgumentParser(prog = 'fix_radio', description = 'This program fixes the radio by finding the end of the required token')
    parser.add_argument("filename", type=FileType("r"))
    args = parser.parse_args()

    with args.filename as f:
        datastream_buffer = f.read().strip()
    print(find_token_end(datastream_buffer, PACKET_LENGTH))
    print(find_token_end(datastream_buffer, MESSAGE_LENGTH))
