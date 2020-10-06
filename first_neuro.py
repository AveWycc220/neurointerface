import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

""" CONST """ 
WIDTH = 12
HEIGHT = 8


if __name__ == "__main__":
    path = "F://Projects//neuro//"
    first_signal_opened = []
    second_signal_opened = []
    third_signal_opened = []
    values_list = None
    with open(path + 'openedEyes.asc') as file:
        for elem in file.read().split('\n'):
            values_list = elem.split(' ')
            if len(values_list) == 3:
                first_signal_opened.append(values_list[0])
                second_signal_opened.append(values_list[1])
                third_signal_opened.append(values_list[2])
    first_signal_opened = (abs(np.fft.fft(first_signal_opened)) ** 2)
    second_signal_opened = (abs(np.fft.fft(second_signal_opened)) ** 2)
    third_signal_opened = (abs(np.fft.fft(third_signal_opened)) ** 2)
    path = "F://Projects//neuro//"
    first_signal_closed = []
    second_signal_closed = []
    third_signal_closed= []
    values_list = None
    with open(path + 'closedEyes.asc') as file:
        for elem in file.read().split('\n'):
            values_list = elem.split(' ')
            if len(values_list) == 3:
                first_signal_closed.append(values_list[0])
                second_signal_closed.append(values_list[1])
                third_signal_closed.append(values_list[2])
    first_signal_closed = (abs(np.fft.fft(first_signal_closed)) ** 2)
    second_signal_closed = (abs(np.fft.fft(second_signal_closed)) ** 2)
    third_signal_closed = (abs(np.fft.fft(third_signal_closed)) ** 2)
    sns.set()
    plt.figure(figsize=(WIDTH,HEIGHT))
    plt.plot(first_signal_opened[3:105])
    plt.plot(first_signal_closed[3:105])
    plt.legend(['Opened', 'Closed'])
    plt.title('First Signal')
    plt.subplot()
    plt.figure(figsize=(WIDTH,HEIGHT))
    plt.plot(second_signal_opened[3:105])
    plt.plot(second_signal_closed[3:105])
    plt.legend(['Opened', 'Closed'])
    plt.title('Second Signal')
    plt.figure(figsize=(WIDTH,HEIGHT))
    plt.plot(third_signal_opened[3:105])
    plt.plot(third_signal_closed[3:105])
    plt.legend(['Opened', 'Closed'])
    plt.title('Third Signal')
    plt.show()