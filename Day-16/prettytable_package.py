from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Guitars", ["Ibanez", "Fender", "Gibson"])
table.add_column("Drums", ["Ludwig", "Sonor", "Mapex"])

print(table)
