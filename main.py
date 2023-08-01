import json
import csv

reader = csv.reader
path_str = input("Input path: ")
with open(f"{path_str}", "r") as this_csv:
    reader=csv.reader(this_csv)
    header_row=reader.__next__()
    name_header_list = list()
    for element in header_row:
        new_dict = {"Name": element, "Type": "STRING}
        name_header_list.append(new_dict)
    print(json.dumps(name_header_list, indent=4))
