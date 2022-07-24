from src.utils.Plants import *
from random import choice, random


class GeneticAlgorithm:

    def __init__(self):
        self.mutation_probability = 0.1
        self.stop_condition = stop_condition

    def selection_strategy(self, generation: BaseField):
        maximum_selected_items = int(len(generation) / 10)
        sorted_elements = sorted(generation, key=lambda x: x.evaluation)
        return sorted_elements[:maximum_selected_items]

    def _generate_random_plants(self):
        plant_names = [choice(BaseField.possibilities) for _ in range(9)]
        return [plant_selector(plant_name) for plant_name in plant_names]

    def _generate_first_population(self):
        return [BaseField(self._generate_random_plants()) for _ in range(15)]

    def run(self) -> BaseField:
        first_population = self._generate_first_population()
        first_population.sort(key=lambda x: x.evaluation)
        population_length = len(first_population)
        i = 0
        while True:
            selected = self.selection_strategy(first_population)
            new_population = selected.copy()
            while len(new_population) != population_length:
                child = choice(first_population).crossover(choice(first_population))
                propability = random()
                if propability <= self.mutation_probability:
                    child.mutate()
                new_population.append(child)

            first_population = new_population
            best_match = min(first_population, key=lambda x: x.evaluation)
            i += 1
            if self.stop_condition(float(best_match)):
                break
        print(f'Best match is {best_match} with {i} iterations')
        return best_match

    def get_plants(self) -> list:
        result_array = []
        for i in range(4):
            result_array = result_array + self.run().plants
        return result_array


def main():
    result_array = []
    genetic_algorithm = GeneticAlgorithm()
    for i in range(4):
        result_array = result_array + genetic_algorithm.run().plants
    print(result_array)


if __name__ == '__main__':
    main()
