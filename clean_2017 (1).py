import csv

def is_number(s):
    try:
        x=float(s)
        if x<1:return False
        return True
    except ValueError:
        return False

with open('2017 (1).csv', 'r') as input_file, open('2017.csv', 'w', newline='') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    for row in reader:
        if all(is_number(cell) for cell in row):
          row.pop(-1)
          row.insert(3,"0")
          row.insert(7,"0")
          row.insert(8,"0")
          row.insert(9,"0")

          writer.writerow(row)
