# functions go here
def selection_sort(data, index = 0):
    """Data should be a nested list, index should be the desired sort position"""
    for start_index in range(len(data) - 1):
        # Find index of smallest remaining element
        smallest_index = start_index
        for i in range(start_index + 1, len(data)):
            if data[smallest_index][index] > data[i][index]:
                smallest_index = i

        # Swap numbers[start_index] and numbers[smallest_index]
        data[start_index], data[smallest_index] = data[smallest_index], data[start_index]
    
    return data

def insertion_sort(data, index = 0):
    """Data should be a nested list, index should be the desired sort position"""
    for start_index in range(len(data)):
        smallest_index = start_index   # starting point

        # slide smallest_index down until we find the last "smallest" value    
        while smallest_index > 0 and data[start_index][index] < data[smallest_index - 1][index]: 
            smallest_index -= 1

        # insert the unsorted item (at start_index) in the "smallest" index (at smallest_index)
        data.insert(smallest_index, data.pop(start_index))
    
    return data

# main
if __name__ == "__main__":
    workers = [["Carmen", "CEO", 51], 
            ["Beto", "Lawyer", 37], 
            ["Davud", "Painter", 31], 
            ["Alex", "Instructor", 42]]

    cars = [["Subaru", "Forester", 2021, 25000, 12672],
            ["Ford", "Explorer", 2024, 35000, 3977],
            ["Nissan", "Altima", 2016, 8500, 87112],
            ["Toyota", "Camry", 2023, 24000, 10936],
            ["Hyundai", "Ioniq", 2025, 42000, 5]]

    # test code
    print(selection_sort(workers, 1))
    print(insertion_sort(cars, 4))

    # code to convert

    # Code for Selection Sort
    for start_index in range(len(workers) - 1):
    # Find index of smallest remaining element
        smallest_index = start_index
        for index in range(start_index + 1, len(workers)):
            if workers[smallest_index][2] > workers[index][2]:
                smallest_index = index

    # Swap numbers[start_index] and numbers[smallest_index]
    workers[start_index], workers[smallest_index] = workers[smallest_index], workers[start_index]

    # Code for Insertion Sort
    for start_index in range(len(workers)):
        smallest_index = start_index   # starting point

        # slide smallest_index down until we find the last "smallest" value    
        while smallest_index > 0 and workers[start_index][2] < workers[smallest_index - 1][2]: 
            smallest_index -= 1

        # insert the unsorted item (at start_index) in the "smallest" index (at smallest_index)
        workers.insert(smallest_index, workers.pop(start_index))
