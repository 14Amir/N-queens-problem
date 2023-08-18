import random

# Define the size of the board
BOARD_SIZE = int(input('Board size: '))

# Define the number of individuals in the population
POPULATION_SIZE = 500

# Define the maximum number of generations to run
MAX_GENERATIONS = 2000

# Define the mutation rate
MUTATION_RATE = 0.5

# Define the fitness function
def fitness(board):
    # Count the number of conflicts
    conflicts = 0
    for i in range(BOARD_SIZE):
        for j in range(i+1, BOARD_SIZE):
            if board[i] == board[j] or abs(board[i]-board[j]) == j-i: # if this second condition be right we have conflict in digonals 
                conflicts += 1
    return 1/(conflicts+1)

# Define the selection function
def selection(population, size):
    # Sort the population by fitness
    sorted_population = sorted(population, key=lambda x: fitness(x), reverse=True)
    # Select the best individuals for reproduction
    selected_population = sorted_population[:size]
    return selected_population

# Define the crossover function
def crossover(parent1, parent2):
    # Choose a random crossover point
    crossover_point = random.randint(1, BOARD_SIZE-1)
    # Create the child by swapping the parents'boards at the crossover point
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

# Define the mutation function
def mutation(board):
    if random.random() < MUTATION_RATE:
        # Choose a random position to mutate
        mutation_point = random.randint(0, BOARD_SIZE-1)
        # Choose a random new value for the position
        new_value = random.randint(0, BOARD_SIZE-1)
        # Mutate the board by changing the value at the mutation point
        board[mutation_point] = new_value
    return board

# Initialize the population with random boards
population = [[random.randint(0, BOARD_SIZE-1) for i in range(BOARD_SIZE)] for j in range(POPULATION_SIZE)]

# prints given chromosome board
def print_board(chrom):
    board = []

    for x in range(BOARD_SIZE):
        board.append(["x"] * BOARD_SIZE)

    for i in range(BOARD_SIZE):
        board[i][chrom[i]] = "Q"

    def print_board(board):
        for row in board:
            print(" ".join(row))

    print()
    print_board(board)

# Run the genetic algorithm
for generation in range(MAX_GENERATIONS):
    # Select the best individuals for reproduction
    selected_population = selection(population, int(POPULATION_SIZE/2))
    # Create new individuals by crossover and mutation
    children = []
    for i in range(int(POPULATION_SIZE/4)):
        parent1 = random.choice(selected_population)
        parent2 = random.choice(selected_population)
        child1 = crossover(parent1, parent2)
        child2 = crossover(parent2, parent1)
        children.append(mutation(child1))
        children.append(mutation(child2))
    # Add the new individuals to the population
    population_init = population + children
    population = selection(population_init, POPULATION_SIZE)
    # Print the best solution so far
    best_solution = max(population, key=lambda x: fitness(x))
    if fitness(best_solution) == 1:
        print("Solution found in generation", generation)
        print(best_solution)
        print_board(best_solution)
        break

# If no solution was found, print the best solution found
else:
    print("Best solution found:")
    print(best_solution)
    print_board(best_solution)