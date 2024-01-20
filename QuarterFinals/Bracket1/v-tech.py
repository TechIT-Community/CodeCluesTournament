import math

class City:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def distance_to(self, other_city):
        x_distance = abs(self.x - other_city.x)
        y_distance = abs(self.y - other_city.y)
        return math.sqrt(x_distance ** 2 + y_distance ** 2)

class Route:
    def __init__(self, cities):
        self.cities = cities

    def total_distance(self):
        return sum(self.cities[i].distance_to(self.cities[i + 1]) for i in range(len(self.cities) - 1)) + \
               self.cities[-1].distance_to(self.cities[0])

class GeneticAlgorithm:
    TOURNAMENT_SIZE = 5
    ELITISM = True

    def __init__(self, initial_route, population_size, generations):
        self.initial_route = initial_route
        self.population_size = population_size
        self.generations = generations

    def evolve_route(self):
        population = [Route(self.initial_route.cities[:]) for _ in range(self.population_size)]

        for _ in range(self.generations):
            population = self.evolve_population(population)

        return min(population, key=lambda route: route.total_distance())

    def evolve_population(self, population):
        new_population = []

        if self.ELITISM:
            new_population.append(min(population, key=lambda route: route.total_distance()))

        while len(new_population) < len(population):
            parent1 = self.tournament_selection(population)
            parent2 = self.tournament_selection(population)
            child = self.crossover(parent1, parent2)
            self.mutate(child)
            new_population.append(child)

        return new_population

    def tournament_selection(self, population):
        tournament = population[:self.TOURNAMENT_SIZE]
        return min(tournament, key=lambda route: route.total_distance())

    def crossover(self, parent1, parent2):
        cities_set = set(parent1.cities)

        child_cities = [city for city in parent2.cities if city in cities_set]
        remaining_cities = [city for city in parent1.cities if city not in child_cities]

        return Route(child_cities + remaining_cities)

    def mutate(self, route):
        # Swap the order of two random cities without using random.sample
        index1, index2 = 0, 0
        while index1 == index2:
            indices = list(range(len(route.cities)))
            index1, index2 = indices[0], indices[1]

        route.cities[index1], route.cities[index2] = route.cities[index2], route.cities[index1]

# Example Usage
cities = [City("A", 0, 0), City("B", 1, 2), City("C", 4, 3), City("D", 7, 8), City("E", 2, 9)]
initial_route = Route(cities)

genetic_algo = GeneticAlgorithm(initial_route, population_size=50, generations=1000)
final_route = genetic_algo.evolve_route()

print("Optimized Route:", [city.name for city in final_route.cities])
print("Optimized Distance:", final_route.total_distance())
