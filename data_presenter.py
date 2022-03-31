# Loop through data from CupcakeInvoices.csv and print each row.
cupcake_file = open("CupcakeInvoices.csv")

for row in cupcake_file: 
    print(row)

# Loop through all the data and print out the total for each invoice
# you will need to convert it to a float
for flavor in cupcake_file:
    vals = flavor.split(',')
    print(vals[2])

# Loop through all the data and print the type of cupcakes purchased.
for cupcake in cupcake_file:
    cupcake = cupcake.strip()
    print(cupcake)
     

# Loop through all the data, and print out the total for all invoices combined.
for totalInvoice in cupcake_file:
    totalInvoice = float(totalInvoice)
    total = total + totalInvoice
    print(total)


# Display the total income of chocolate cupcakes vs vanilla cupcakes vs strawberry cupcakes.
chocolate_income = 0
vanilla_income = 0
strawberry_income = 0

for income in cupcake_file:
    income = float(income)
    if "Chocolate" in income:
        chocolate_income = chocolate_income + income
    elif "Vanilla" in income:
        vanilla_income = vanilla_income + income
    elif "Strawberry" in income:
        strawberry_income = strawberry_income + income
    else:
        print("Not found")

    print(chocolate_income, vanilla_income, strawberry_income)


cupcake_file.close()