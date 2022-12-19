from dataclasses import dataclass
from typing import List, Tuple

FACES_OF_CUBE = [
    (0, 0, 1),
    (0, 0, -1),
    (0, 1, 0),
    (0, -1, 0),
    (1, 0, 0),
    (-1, 0, 0)
]

@dataclass()
class Cube:
    x: int
    y: int
    z: int

    def __repr__(self) -> str:
        return f"X: {self.x}, Y: {self.y}, Z: {self.z}"

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Cube):
            return self.x == __o.x and self.y == __o.y and self.z == __o.z
        else:
            return NotImplemented

@dataclass
class Face:
    first_cube: Cube
    second_cube: Cube

    def __repr__(self) -> str:
        return f"Face for cube {self.first_cube} and cube {self.second_cube}"

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Face):
            return self.first_cube == __o.first_cube and self.second_cube == __o.second_cube
        else:
            return NotImplemented

    def __hash__(self) -> int:
        return hash((self.first_cube, self.second_cube))

def generate_faces_from_cube(cube: Cube) -> List[Tuple[Cube]]:
    # Each face is identified uniquely by the coordinates of the two voxels that this face is part of, ordered.
    faces = []
    for face in FACES_OF_CUBE:
        if sum(face) > 0:
            faces.append(Face(cube, Cube(cube.x + face[0], cube.y + face[1], cube.z + face[2])))
        elif sum(face) < 0:
            faces.append(Face(Cube(cube.x + face[0], cube.y + face[1], cube.z + face[2]), cube))
        else:
            raise Exception("There’s a problem with your face.")
    return faces
