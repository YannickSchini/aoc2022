from argparse import ArgumentParser, FileType

if __name__ == "__main__":
    parser = ArgumentParser(prog = "TODO", description = "TODO")
    parser.add_argument("filename", type=FileType("r"))
    args = parser.parse_args()

    with args.filename as f:
        lines = list(map(str.strip, f.readlines()))
