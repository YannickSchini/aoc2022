from typing import List, Callable, Dict


class Monkey:

    instances = []
    OPERATIONS: Dict[str, Callable] = {"+": int.__add__, "*": int.__mul__}

    def __init__(self, raw_monkey_descr: List[str]):
        self.__class__.instances.append(self)
        self.name: str = raw_monkey_descr[0][:-1]
        self.starting_items: List[int] = self._get_starting_items_from_raw(raw_monkey_descr[1])
        self.operation_func: Callable = self._get_operation_from_raw(raw_monkey_descr[2])
        self.test_func: Callable = self._get_test_from_raw(raw_monkey_descr[3])
        self.target_func: Callable = self._get_target_from_raw(raw_monkey_descr[4:])
        self.number_of_inspections = 0

    def __del__(self):
        self.__class__.instances.remove(self)

    def __repr__(self):
        repr_str = f"{self.name}"
        repr_str += "\n"
        repr_str += f"\tStarting_items: {self.starting_items}"
        repr_str += "\n"
        return repr_str

    def _get_starting_items_from_raw(self, raw_starting_items: str) -> List[int]:
        raw_items = raw_starting_items.split(": ")[1]
        return list(map(int, raw_items.split(", ")))

    def _get_operation_from_raw(self, raw_operation: str) -> Callable:
        elements = raw_operation.strip().split(" ")
        if elements[3] == "old" and elements[5] == "old":
            return lambda x: self.OPERATIONS[elements[4]](x, x)
        else:
            return lambda x: self.OPERATIONS[elements[4]](x, int(elements[5]))

    def _get_test_from_raw(self, raw_test: str) -> Callable:
        elements = raw_test.strip().split(" ")
        return lambda x: int.__mod__(x, int(elements[3])) == 0

    def _get_target_from_raw(self, raw_target: List[str]) -> Callable:
        elements_0 = raw_target[0].strip().split(" ")
        elements_1 = raw_target[1].strip().split(" ")
        return lambda x: elements_0[-1] if x else elements_1[-1]

    def test(self, value: int) -> bool:
        return self.test_func(value)

    def increase_stress(self, value: int) -> int:
        self.number_of_inspections += 1
        return self.operation_func(value)

    def get_target(self, value: int):
        target_str = self.target_func(self.test(value))
        for monkey in self.__class__.instances:
            if monkey.name == "Monkey " + target_str:
                return monkey
            else:
                Exception("Unknown targe Monkey !")

    def turn(self) -> None:
        for item in self.starting_items.copy():
            # print("Current item/stress lvl before inspection: ", item)
            stress_lvl_due_to_inspection = self.increase_stress(item)
            # print("Current item/stress lvl after inspection: ", stress_lvl_due_to_inspection)
            stress_lvl_after_relief = stress_lvl_due_to_inspection//3
            # print("Current item/stress lvl after relief: ", stress_lvl_after_relief)
            target = self.get_target(stress_lvl_after_relief)
            # print(f"Target monkey {target} for the item {stress_lvl_after_relief}")
            target.starting_items.append(stress_lvl_after_relief)
            self.starting_items.remove(item)
