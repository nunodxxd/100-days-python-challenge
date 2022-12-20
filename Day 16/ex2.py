from prettytable import PrettyTable

table = PrettyTable()
# add rows
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "bulbasaur"])
table.add_column("Type", ["Electric", "Water", "Grass"])
# left align
table.align = "l" 

print(table)
