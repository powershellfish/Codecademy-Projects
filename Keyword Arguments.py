#An exercist in concatenating a string to an object
#INCORRECT

# Define create_spreadsheet():
def create_spreadsheet(title, row_count=1000):
  print("Creating a spreadsheet called "+title, "with", +row_count str("rows"))

# Call create_spreadsheet() below with the required arguments:
create_spreadsheet("Downloads")


#CORRECT
def create_spreadsheet(title, row_count = 1000):
  print("Creating a spreadsheet called "+title+" with "+str(row_count)+" rows.")
  
create_spreadsheet("Downloads")
create_spreadsheet("Applications", 10)