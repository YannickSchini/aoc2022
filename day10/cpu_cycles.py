from argparse import ArgumentParser, FileType
from typing import List, Dict


def process_instructions(instructions: List[str]) -> Dict[int, int]:
    register_value_changes = {}
    current_cpu_cycle = 1
    current_register_value = 1
    for instruction in instructions:
        if instruction == "noop":
            current_cpu_cycle += 1
        elif instruction.startswith("addx "):
            value = instruction.split(" ")[1]
            current_register_value += int(value)
            current_cpu_cycle += 2
            register_value_changes[current_cpu_cycle] = current_register_value
        else:
            Exception("Unknown CPU instruction.")
    return register_value_changes


def get_signal_strength(cpu_cycle: int, register: int) -> int:
    return cpu_cycle * register


if __name__ == "__main__":
    parser = ArgumentParser(prog="cpu_cycles", description="Calculate register value for each CPU cycle")
    parser.add_argument("filename", type=FileType("r"))
    args = parser.parse_args()

    with args.filename as f:
        instructions = list(map(str.strip, f.readlines()))

    register_value_changes = process_instructions(instructions)

    signal_strength = 0
    cpu_cycle = 1
    register = 1
    while True:
        try:
            register = register_value_changes[cpu_cycle]
        except KeyError:
            pass
        if cpu_cycle % 40 == 20:
            signal_strength += get_signal_strength(cpu_cycle, register)
        cpu_cycle += 1
        if cpu_cycle > max(register_value_changes.keys()):
            break
    print("Part 1: ", signal_strength)
