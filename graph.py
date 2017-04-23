from collections import Counter

import csv
import matplotlib.pyplot as plt
import numpy as np
import parse as parse

MY_FILE = "/Users/Saturnist/Google Drive/program/learn_python/dataviz/data/sample_sfpd_incident_all.csv"

def visualize_days():
    """Visualize data by day of week"""
    data_file = parse(MY_FILE, ",")
    counter = Counter(item["DayOfWeek"] for item in data_file)
    data_list = [
        counter["Monday"],
        counter["Tuesday"],
        counter["Wednesday"],
        counter["Thursday"],
        counter["Friday"],
        counter["Saturday"],
        counter["Sunday"]
    ]
    day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

    plt.plot(data_list)

    plt.xticks(range(len(day_tuple)), day_tuple)

    plt.savefig("Days.png")
    plt.clf()

def visualize_type():
    """Visualize data by category in a bar graph"""
    data_file = parse(MY_FILE, ",")
    counter = Counter(item["Category"] for item in data_file)

    labels = tuple(counter.keys())

    xlocations = np.arange(len(labels)) + 0.5

    width = 0.5

    plt.bar(xlocations, counter.values(), width=width)

    plt.xticks(xlocations + width / 2, labels, rotation=90)

    plt.subplots_adjust(bottom=0.4)

    plt.rcParams['figure.figsize'] = 12, 8

    plt.savefig("Type.png")

    plt.clf()

def main():
    visualize_days()
    visualize_type()

if __name__ == "__main__":
    main()