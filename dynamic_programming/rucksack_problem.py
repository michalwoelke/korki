def main():
    items = [Item("stereo", 3000, 4),
             Item("laptop", 2000, 3),
             Item("guitar", 1500, 1),
             Item("iPhone", 2000, 1),
             Item("mp3", 1000, 1),
             Item("ring", 2000, 0.5)]
    print(find_most_value_rucksack(items, 5))


def find_most_value_rucksack(items: list, rucksack_max_capacity):
    best_values = {i / 2: RucksackCell(0, []) for i in range(1, 2 * rucksack_max_capacity + 1)}
    for item in items:
        new_best_values = {}
        for r_c in range(1, 2 * rucksack_max_capacity + 1):
            rucksack_capacity = r_c / 2
            if item.mass > rucksack_capacity:
                new_best_values[rucksack_capacity] = best_values[rucksack_capacity]
            else:
                free_capacity = rucksack_capacity - item.mass
                value_if_curr_item_taken = item.value
                if free_capacity > 0:
                    value_if_curr_item_taken += best_values[free_capacity].value
                if value_if_curr_item_taken > best_values[rucksack_capacity].value:
                    new_best_items = [item]
                    if free_capacity > 0:
                        new_best_items.extend(best_values[free_capacity].items)
                    new_best_values[rucksack_capacity] = RucksackCell(value_if_curr_item_taken, new_best_items)
                else:
                    new_best_values[rucksack_capacity] = best_values[rucksack_capacity]
        best_values = new_best_values
    return best_values[rucksack_max_capacity]


class RucksackCell:
    def __init__(self, value: int, items: list):
        self.value = value
        self.items = items

    def __str__(self):
        return f'val= {self.value}, items= {self.items}'


class Item:
    def __init__(self, name, value, mass):
        self.name = name
        self.value = value
        self.mass = mass

    def __str__(self):
        return f'name= {self.name}'

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    main()
