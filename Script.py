import gspread 
import random

sa=gspread.service_account(filename="negotiation-skills-splitter-6eea93569238.json")
sh=sa.open("Negotiation Skills  (Responses)")

wks=sh.worksheet("Form Responses 1")

#collect all the names
name_column = wks.col_values(2)  

#Removes Header Value
name_column = name_column[1:]

# Initialize Buyer and Seller lists
buyer_column = []
seller_column = []

# Create headers for the Buyer and Seller columns
wks.update('C1', [['Buyer']])
wks.update('D1', [['Seller']])

#Splitting Randomly Logic 
random.shuffle(name_column)

# Iterate through shuffled names and assign them alternately to Buyer and Seller
for i, name in enumerate(name_column):
    if i % 2 == 0:
        buyer_column.append([name])
    else:
        seller_column.append([name])

print(buyer_column)
print(seller_column)

# Update the worksheet with the Buyer and Seller columns
wks.update('C2', buyer_column)
wks.update('D2', seller_column)

print("Buyer and Seller columns added to the existing worksheet.")

