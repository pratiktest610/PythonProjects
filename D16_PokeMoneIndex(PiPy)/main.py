from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Name",["Pikachu", "Charmender", "Kadabra"])
table.add_column("Type",["Electric", "Fire", "Pshycic"])
table.align = "l"
print(table)