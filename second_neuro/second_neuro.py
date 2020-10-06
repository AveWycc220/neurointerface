import numpy as np
import openpyxl

""" CONST """
TICKRATE = 0.01

def read_file(N = 0):
    path = "F://Projects//neuro//"
    first_signal_opened = []
    second_signal_opened = []
    third_signal_opened = []
    values_list = None
    with open(path + 'openedEyes.asc') as file:
        for elem in file.read().split('\n'):
            values_list = elem.split(' ')
            if len(values_list) == 3:
                first_signal_opened.append(int(values_list[0]))
                second_signal_opened.append(int(values_list[1]))
                third_signal_opened.append(int(values_list[2]))
                if len(first_signal_opened) == N and N != 0: 
                    break
    first_signal_closed = []
    second_signal_closed = []
    third_signal_closed= []
    values_list = None
    with open(path + 'closedEyes.asc') as file:
        for elem in file.read().split('\n'):
            values_list = elem.split(' ')
            if len(values_list) == 3:
                first_signal_closed.append(int(values_list[0]))
                second_signal_closed.append(int(values_list[1]))
                third_signal_closed.append(int(values_list[2]))
                if len(first_signal_closed) == N and N != 0: 
                    break
    signal_list = [first_signal_opened, second_signal_opened, third_signal_opened, \
    first_signal_closed, second_signal_closed, third_signal_closed]
    return signal_list

def correlation(first_signal, second_signal):
    first_signal_average = 0
    second_signal_average = 0
    for i in range(0, len(first_signal)):
        first_signal_average += first_signal[i]
    first_signal_average /= len(first_signal)
    for i in range(0, len(second_signal)):
        second_signal_average += second_signal[i]
    second_signal_average /= len(second_signal)
    numerator = 0
    denominator_left = 0
    denominator_right = 0
    for i in range(0, len(first_signal)):
        numerator += (first_signal[i] - first_signal_average) * (second_signal[i] - second_signal_average)
        denominator_left += ((first_signal[i] - first_signal_average) ** 2)
        denominator_right += ((second_signal[i] - second_signal_average) ** 2)
    return numerator/np.sqrt(denominator_left * denominator_right)

if __name__ == "__main__":
    wb = openpyxl.load_workbook(filename = 'F:\\Projects\\neuro\\second_neuro\\correlation.xlsx')
    sheet = wb['Лист1']
    time = [0.1, 0.2, 0.5, 1, 2, 3]
    count = 0
    ticks = []
    for item in time:
        ticks.append(item/TICKRATE)
    for item in ticks:
        signal_list = read_file(item)
        for i in range(2, 8):
            for j in range(2, 8):
                if i == j:
                    sheet.cell(row = i + count, column= j).value = '-----------------'
                else:
                    print(f'{i-1} | {j-1} | {correlation(signal_list[i-2], signal_list[j-2])}')
                    sheet.cell(row = i + count, column = j).value = correlation(signal_list[i-2], signal_list[j-2])
        count += 7
    wb.save('F:\\Projects\\neuro\\second_neuro\\correlation.xlsx')