# 18.3 Table print

import retail_dataset

# table_print takes a nested list, header row, and column width
# Prints out a double column table
def table_print(headers, data, width = 15):
    total_width = width * len(headers)
    for header in headers:
        print(f"{header :<{width}}", end="")
    print()
    print("-" * total_width)
    for item in sorted(data):
        for info in item:
            print(f"{info :<{width}}", end="")
        print()
    print()

# main
if __name__ == "__main__":
    labels = ["Name", "Age"]
    people = [("Sam", 20), ("Juniper", 18), ("Adam", 22), ("Susan", 19), ("Daniel", 21)]

    labels2 = ["Capital", "State"]
    states = [("Atlanta", "GA"), ("Boston", "MA"), ("Columbus", "OH"), ("Austin", "TX"), ("Boise", "ID")]

    table_print(labels, people)
    table_print(labels2, states, 15)
    table_print(retail_dataset.labels,retail_dataset.data)



