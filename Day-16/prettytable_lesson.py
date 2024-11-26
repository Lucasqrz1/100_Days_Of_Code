from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Guitar brands", ["Ibanez", "Fender", "Gibson"])
table.add_column("Drum brands", ["Ludwig", "Sonor", "Mapex"])

table.align= "c"
print(table)
