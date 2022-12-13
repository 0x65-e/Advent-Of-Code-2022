from typing import Optional

class Directory:
    def __init__(self, name: str, parent=None):
        self._parent = parent
        self._name = name
        self._entries = dict()
        self._subdirectories = dict()

    def get_name(self) -> str:
        return self._name

    def add_file(self, file_name: str, file_size: int) -> None:
        self._entries[file_name] = file_size

    def add_subdirectory(self, subdirectory: str) -> None:
        self._subdirectories[subdirectory] = Directory(subdirectory, self)

    def get_subdirectory(self, subdirectory: str):
        return self._subdirectories[subdirectory]

    def get_parent(self):
        return self._parent

    def get_size(self) -> int:
        total_size = sum(self._entries.values())
        for subdir in self._subdirectories.values():
            total_size += subdir.get_size()
        return total_size

    def get_size_limit(self, limit: Optional[int]):
        directory_list = list()
        self._get_size_limit_recursive(limit, directory_list)
        return directory_list

    def _get_size_limit_recursive(self, limit: Optional[int], directories: list) -> int:
        total_size = sum(self._entries.values())
        for subdir in self._subdirectories.values():
            total_size += subdir._get_size_limit_recursive(limit, directories)
        if limit == None or total_size <= limit:
            directories.append((self, total_size))
        return total_size

def populate_filesystem(input: list[str]):
    current_dir = None
    root_dir = None
    for line in input:
        if line.startswith("$ cd"):
            dirname = line[5:]
            if current_dir == None:
                current_dir = Directory(dirname)
                root_dir = current_dir
            elif dirname == "..":
                current_dir = current_dir.get_parent()
            else:
                current_dir = current_dir.get_subdirectory(dirname)
        elif line.startswith("dir "):
            current_dir.add_subdirectory(line[4:])
        elif line[0].isnumeric():
            file_size, file_name = line.split(" ")
            file_size = int(file_size)
            current_dir.add_file(file_name, file_size)
    return root_dir

def solve07_p1(root_dir) -> None:
    small_directories = root_dir.get_size_limit(100000)
    total_size = sum([ dirent[1] for dirent in small_directories ])
    print("Sum of small directories: {}".format(total_size))

def solve07_p2(root_dir) -> None:
    all_directories = root_dir.get_size_limit(None)
    dir_sizes = [ dirent[1] for dirent in all_directories ]
    used_space = max(dir_sizes)
    print("Space used: {}".format(used_space))
    necessary_free_space = max(used_space - 40000000, 0)
    solutions = [ size for size in dir_sizes if size >= necessary_free_space ]
    print("Smallest directory to remove: {}".format(min(solutions)))

if __name__ == "__main__":
    with open("../inputs/input07.txt") as input_file:
        input = input_file.read().splitlines() # Strip trailing newlines
    root_dir = populate_filesystem(input)
    print("Part 1 solution:")
    solve07_p1(root_dir)
    print("\nPart 2 solution:")
    solve07_p2(root_dir)
