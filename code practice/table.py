from tabulate import tabulate
data = [["Name", "Place", "Gender"], 
        ["Broke", "New Jearsy", "Male"], 
        ["Vasilika", "Athena", "Female"], 
        ["Boraev", "NY", "Male"]]
print(tabulate(data))

# --------  ----------  ------
# Name      Place       Gender
# Broke     New Jearsy  Male  
# Vasilika  Athena      Female
# Boraev    NY          Male  
# --------  ----------  ------



print(tabulate(data, headers='firstrow'))
# Name      Place       Gender  
# --------  ----------  --------
# Broke     New Jearsy  Male    
# Vasilika  Athena      Female  
# Boraev    NY          Male    



print(tabulate(data, headers='firstrow', tablefmt='grid'))

# +----------+------------+----------+
# | Name     | Place      | Gender   |
# +==========+============+==========+
# | Broke    | New Jearsy | Male     |
# +----------+------------+----------+
# | Vasilika | Athena     | Female   |
# +----------+------------+----------+
# | Boraev   | NY         | Male     |
# +----------+------------+----------+


print(tabulate(data, headers='firstrow', tablefmt='fancy_grid'))

# ╒══════════╤════════════╤══════════╕
# │ Name     │ Place      │ Gender   │
# ╞══════════╪════════════╪══════════╡
# │ Broke    │ New Jearsy │ Male     │
# ├──────────┼────────────┼──────────┤
# │ Vasilika │ Athena     │ Female   │
# ├──────────┼────────────┼──────────┤
# │ Boraev   │ NY         │ Male     │
# ╘══════════╧════════════╧══════════╛