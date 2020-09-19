import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    path = "/home/aleksey/Рабочий стол/neuro/"
    first_signal = []
    second_signal = []
    third_signal = []
    values_list = None
    with open(path + 'openedEyes.asc') as file:
        for elem in file.read().split('\n'):
            values_list = elem.split(' ')
            print(values_list)
            if len(values_list) == 3:
                first_signal
    print(values_list)