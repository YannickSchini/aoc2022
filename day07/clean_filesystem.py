from argparse import ArgumentParser, FileType
from typing import List
from anytree import Node, RenderTree, PostOrderIter

DIRECTORY_SIZE_LIMIT = 100000
TARGET_FREE_SPACE = 30000000
TOTAL_FILE_SYSTEM_CAPACITY = 70000000

def build_filesystem_tree(filesystem_commands: List[str]) -> Node:
    current_node = None
    for command in filesystem_commands:
        if command.startswith("$ cd "):
            if command == "$ cd ..":
                current_node = current_node.parent
            elif not current_node:
                target = command.split(" ")[2]
                root = Node(target, size=None)
                current_node = root
            elif command == "$ cd /":
                current_node = root
            else:
                target = command.split(" ")[2]
                new_node = Node(target, parent=current_node, size=None)
                current_node = new_node
        elif command.startswith("$ ls"):
            pass
        elif command.startswith("dir"):
            pass
        else:
            size, file_name = command.split(" ")
            new_node = Node(file_name, parent=current_node, size=size)
    return root

def enrich_tree_with_dir_size(tree_root: Node) -> Node:
    for node in PostOrderIter(tree_root):
        if node.size:
            pass
        else:
            node.size = 0
            for child in node.children:
                node.size += int(child.size)
    return tree_root

def find_dirs_below_size_limit(tree_root: Node, size_limit: int) -> List[Node]:
    dirs = []
    for node in PostOrderIter(tree_root):
        if node.children == ():
            pass
        elif node.size <= size_limit:
            dirs.append(node)
        else:
            pass
    return dirs

def find_dirs_above_size_limit(tree_root: Node, size_limit: int) -> List[Node]:
    dirs = []
    for node in PostOrderIter(tree_root):
        if node.children == ():
            pass
        elif node.size > size_limit:
            dirs.append(node)
        else:
            pass
    return dirs

if __name__ == "__main__":
    parser = ArgumentParser(prog = 'fix_radio', description = 'This program fixes the radio by finding the end of the required token')
    parser.add_argument("filename", type=FileType("r"))
    args = parser.parse_args()

    with args.filename as f:
        filesystem_commands = list(map(str.strip, f.readlines()))
    tree_root = build_filesystem_tree(filesystem_commands)
    tree_root = enrich_tree_with_dir_size(tree_root)

    dirs_to_remove = find_dirs_below_size_limit(tree_root, DIRECTORY_SIZE_LIMIT)
    print("Part 1: ", sum([dir.size for dir in dirs_to_remove]))

    print("Total used space: ", tree_root.size)
    space_to_be_freed = abs(TARGET_FREE_SPACE - tree_root.size)
    print("Space to be freed: ", space_to_be_freed)
    # print(find_dirs_above_size_limit(tree_root, space_to_be_freed))
    print("Part 2: ", min([dir.size for dir in find_dirs_above_size_limit(tree_root, space_to_be_freed)]))
