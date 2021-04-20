import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)

    is field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}
        return None

    with open(file_path, "r") as json_file:
        dict = json.load(json_file)

    return dict[field]

def linear_search(sequence, key)
    listx = []
    count = 0

    for idx in range(len(sequence))
        if sequence[idx] == key:
            listx.append(idx)
            count += 1

    return {
        "positions": listx,
        "count":count
    }

def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)

    result = linear_search(sequential_data, 5)
    print(result)
if __name__ == '__main__':
    main()