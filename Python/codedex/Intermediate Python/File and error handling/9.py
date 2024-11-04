import csv

# Open the CSV file in 'read' mode
with open('Bestseller - Sheet1.csv', 'r', encoding='utf8') as file:
  # Create a CSV reader object
  csv_reader = csv.reader(file)

  for row in csv_reader:
    print(row)



with open('bestseller_info.csv', 'w', newline='') as file:
  csv_writer = csv.writer(file)

  csv_writer.writerows(data_to_write)
