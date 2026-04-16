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
    with open(file_path, "r") as file:
        data = json.load(file)
        if field in data:
            return data[field]

def linear_search(sekvence, cislo):
    count = 0
    index = []
    vlv = 0
    cislo_kolikrat = []
    for i in sekvence:
        if i == cislo:
            count += 1
            index.append(vlv)
        vlv += 1
    cislo_kolikrat = count
    plp = set(index)
    return {"positions":index,"count": cislo_kolikrat}

def binary_search(seznam, cislo):
    prostřed = len(seznam) / 2
    stred1 = int(prostřed)
    vlv = seznam[stred1]
    leva = 0
    prava = len(seznam) - 1
    while leva <= prava:
        střed = (leva + prava) // 2
        střed_hodnota = seznam[střed]
        if střed_hodnota == cislo:
            return střed
        elif střed_hodnota < cislo:
            leva = střed + 1
        else:
            prava = střed - 1
    return None



def main():
    sequential_data  = read_data("sequential.json", "unordered_numbers")
    sequential_data2 = read_data("sequential.json", "ordered_numbers")
    print(sequential_data)
    print(sequential_data2)
    print(linear_search( [54, 2, 18, 5, 3, 31, 20, 65, -10, 300, 17, 5, -1, 0, 0, 102, 7, 8, 9, 9, -3, -5, 0, 1, 63, 82, -36, -5], 5))
    print(binary_search(sequential_data2, 13))
    pass


if __name__ == '__main__':
    main()