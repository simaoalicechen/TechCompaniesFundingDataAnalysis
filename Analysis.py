# Tech.csv is a file containing many tech companies' funding information between the year 2004 to 2008
# This project is aimed to study the funding patterns in small/medium tech companies in their early stages 

import csv 
import math
member_company = ['facebook', 'amazon', 'apple', 'netflix', 'google', 'youtube', 'twitter', 'paypal', 'linkedIn', 'hulu']

# Check how many rows and cols there are in the original file 

with open('Tech.csv', 'r') as readFile:
    reader = csv.reader(readFile)
    rows = list(reader)
    header = rows[0]
    col_num = len(header)
    row_num = len(rows)
    print(f"header is {header}\ncol_num is {col_num}\nrow_num is {row_num}")
# Print out the name of each column 

    print(rows[0])

# Extract one company's information and calculate the totle amount raised
# Return a dictionary to contain all the necessary info

def companyFunding_fixed(company_name):
    company_dict = {}
    amount=0
    is_found = 0
    for row in rows[1:]:
        if company_name == row[1]:
            amount = amount + float(row[7])
            company_dict = {'name': row[1],
                    'category': row[3],
                    'city': row[4],
                    'state': row[5],
                    'Total Amount Raised': amount,}
            is_found = 1
    if is_found == 0:
        print(f"The company you are inquiring ({company_name}) is not in this database. Try a different one.")
    else:
        print(company_dict)

    return company_dict

companyFunding_fixed('Amazon')
companyFunding_fixed('Facebook')

# Print out the number of Angel Funding round 

def percentage(num1, num2):
  return str(math.trunc(100 * float(num1)/float(num2)))+"%"



# Exclude rows that have the biggest tech companies
# Print out the number of rows of small/medium tech companies 

for row in rows:
  if row[0] in member_company: 
    rows.remove(row)
    small_medium_tech_rows = list(rows)  
    small_medium_row_num=len(small_medium_tech_rows)
    
print(f"There are {small_medium_row_num} rounds of fundings for small/medium companies in this database. They are {percentage(small_medium_row_num, row_num)} of the total fundings.")


# Return the number of Seed Funding round

def angel_funding(): 
  angel_lines = list()
  for row in small_medium_tech_rows:
    if row[9] == 'angel':
      angel_lines.append(row) 
      angel_row_num=len(angel_lines)
      message = f"Among the {small_medium_row_num} rounds of fundings, {angel_row_num} of them are angel fundings. They represent {percentage(angel_row_num, small_medium_row_num)} of the rounds."
  return message

# Return the number of Seed Funding round

def seed_funding(): 
  seed_lines = list()
  for row in small_medium_tech_rows:
    if row[9] == 'seed':
      seed_lines.append(row) 
      seed_row_num=len(seed_lines)
      message = f"Among the {small_medium_row_num} rounds of fundings, {seed_row_num} of them are seed fundings. They represent {percentage(seed_row_num, small_medium_row_num)} of the rounds."
  return message

# Return the number of series a Funding round

def series_a_funding(): 
  a_lines = list()
  for row in small_medium_tech_rows:
    if row[9] == 'a':
      a_lines.append(row) 
      a_row_num=len(a_lines)
      message = f"Among the {small_medium_row_num} rounds of fundings, {a_row_num} of them are series a fundings. They represent {percentage(a_row_num, small_medium_row_num)} of the rounds."
  return message

# Return the number of series b Funding round

def series_b_funding(): 
  b_lines = list()
  for row in small_medium_tech_rows:
    if row[9] == 'b':
      b_lines.append(row) 
      b_row_num=len(b_lines)
      message = f"Among the {small_medium_row_num} rounds of fundings, {b_row_num} of them are series b foundings. They represent {percentage(b_row_num, small_medium_row_num)} of the rounds."
  return message 

# Return the number of series c Funding round

def series_c_funding(): 
  c_lines = list()
  for row in small_medium_tech_rows:
    if row[9] == 'c':
      c_lines.append(row) 
      c_row_num=len(c_lines)
      message = f"Among the {small_medium_row_num} rounds of fundings, {c_row_num} of them are series c fundings. They represent {percentage(c_row_num, small_medium_row_num)} of rounds."
  return message

# Return the # of rounds that has more than $1m for one funding

def million_dollar_baby(): 
  million_lines = list()
  for row in small_medium_tech_rows:
    if row[7] == 'raisedAmt': 
      continue 
    if int(row[7]) > 1000000: 
      million_lines.append(row) 
      million_row_num=len(million_lines)
      message = f"Among the {small_medium_row_num} rounds of fundings, {million_row_num} companies have more than $1M. They represent {percentage(million_row_num, small_medium_row_num)} of the rounds."
  return message


