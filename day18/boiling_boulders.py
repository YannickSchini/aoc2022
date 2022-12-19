from argparse import ArgumentParser, FileType
from cubes import Cube, generate_faces_from_cube

if __name__ == "__main__":
    parser = ArgumentParser(
        prog="Boiling Boulders",
        description="Calculate the surface area of lava drops")
    parser.add_argument("filename", type=FileType("r"))
    args = parser.parse_args()

    with args.filename as f:
        raw_cubes = list(map(str.strip, f.readlines()))

    faces_used = {}
    for raw_cube in raw_cubes:
        cube = Cube(*list(map(int, raw_cube.split(","))))
        for face in generate_faces_from_cube(cube):
            if face in faces_used.keys():
                faces_used[face] += 1
            else:
                faces_used[face] = 1

    print("Part 1: ", list(faces_used.values()).count(1))
