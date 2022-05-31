# Author: Caoimhin Vallely
# Benchmarking sorting algorithms project
# GMIT HDIP in Data Analytics 2021/2022

# |=========|
# | MODULES |
# |=========|

import time
from random import randint
import pandas as pd
import matplotlib.pyplot as plt
import plots
import algos as al
import numpy as np
import sys

# increasing recursion limit. Default limit of 1000 wasn't enough for my version of quicksort!
# https://stackoverflow.com/questions/3323001/what-is-the-maximum-recursion-depth-in-python-and-how-to-increase-it
sys.setrecursionlimit(3500)

# |===========|
# | VARIABLES |
# |===========|

# dict of sorting algorithims and paths to relevent functions
algorithms = {"Bubble_sort": al.bubbleSort, "Insertion_sort": al.insertionSort, 
            "Merge_sort": al.mergeSort, "Bucket_sort": al.bucketSort, 
            "Quick_sort": al.quickSort}
# list of sizes of arrays to be tested
ars1 = [10, 50, 100, 125, 250, 500, 750, 1000]
ars2 = [500, 750, 1000, 1250, 2500, 3750, 5000, 6750, 7500, 8750, 10000, 20000]
ars3 = [250, 500, 750, 1000, 1500, 3000]
# empty list to take times for each trial
times_elapsed = []
# empty list to record array size
arr_size =[]
# empty list for current trial number for each algorithm
run_no =[]
# empty list to record name of algorithm used
sort_type =[]

# |===========|
# | FUNCTIONS |
# |===========|

# function takes in list of algorithms, list of array sizes, no. of trials, and type of array
def bench(algorithms, ars, runs, z): 
    # loops through the sorting algorithms 
    for algo in algorithms:
        # prints which algorithm is currently running
        print(f"running {algo}") 
        # loops through the array sizes
        for a in ars:
            # loops through everything 'runs' (10) times
            for run in range(runs):
                if z == 1:
                    # creates random arrays between zero and 100 for each of the various sizes of array
                    x = [randint(0,100) for i in range(a)] 
                elif z == 2:
                    x = [randint(0,100) for i in range(a)]
                elif z == 3: 
                    # creates ordered arrays ascending            
                    x = list(range(0, a, 1))
                elif z == 4:
                    # creates ordered arrays desscending  
                    x = list(range(a, -1, -1))               
                elif z == 5:
                    # creates normally distributed random array of integers
                    x = np.random.normal(250, 10, a).round().astype(int)          
                # selects the sorting algorithm to use
                algorithm = algorithms[algo]
                # time function to record start time of sort
                start_time = time.time()
                # runs the algorithm
                algorithm(x)
                # time function to record end time of sort
                end_time = time.time()
                # subtracts start time from end time to get duration
                # multiplied by 1000 to get it in milliseconds
                time_elapsed = (end_time - start_time) * 1000
                # adds duration time to a list
                times_elapsed.append(time_elapsed)          
                # records the current run number
                run_no.append(run+1)
                # records the current array size
                arr_size.append(a)
                # records which algorithm being used
                sort_type.append(algo) 

    # creates a dataframe with the results        
    df = pd.DataFrame({"Algorithm": sort_type, "Array_size": arr_size, "Time": times_elapsed, "Trial_no": run_no})
    return df


# function for calculating averages
def average(df):
    # uses Size column for index
    df.set_index('Array_size', inplace=True)
    # calculate the averages for each sorting algorithm for each array size
    # rounded to 3 decimal points
    avgs = (df.iloc[:, 0:2].groupby(['Algorithm','Array_size']).mean()).round(3)
    # 'unstack' to make 'df' horizontal (https://www.datasciencemadesimple.com/reshape-using-stack-unstack-function-pandas-python/)
    return avgs.unstack()

# function to view results from csv file
def view_averages():
    df = pd.read_csv("results/averages.csv", skiprows = 1, index_col='Array_size')
    df.rename(index = {'Array_size':'Algorithm'}, inplace = True)
    print(df)

# function to view full results from csv file
def view_full_results():
    # https://www.adamsmith.haus/python/answers/how-to-print-an-entire-pandas-dataframe-in-python
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    df = pd.read_csv("results/full_results.csv")
    # renaming columns
    df = df[["Trial_no", "Algorithm", "Array_size", "Time"]]
    print(df)

# 'main' sorting function
def sort(ars, z):
    # sends lists of algorithms, array sizes, and run times to bench function
    full_results = bench(algorithms, ars, 10, z)
    # sends the results to the average() function
    averages = average(full_results)
    # reorders the rows based on predicted performance (https://stackoverflow.com/questions/30009948/how-to-reorder-indexed-rows-based-on-a-list-in-pandas-data-frame)
    averages2 = averages.reindex(["Bubble_sort", "Insertion_sort", "Merge_sort", "Quick_sort", "Bucket_sort"])
    averages2.rename_axis(None, inplace=True)
    averages2.to_csv("results/averages.csv")
    full_results.to_csv("results/full_results.csv")
    # gets rid of unnecessary titles for print purposes    
    averages2.columns = averages.columns.droplevel()
    print(averages2)
    # plots the results
    averages2.T.plot(marker = 'o')
    plt.xlabel("Input size n")
    plt.ylabel("Running time (milliseconds)")
    plt.title("Runtimes for benchmarking sorting algorithms")
    plt.grid()
    plt.show()

# function to choose type of array to benchmark algorithms
def choose():
    print("1. Benchmark algorithms on random low input arrays")
    print("2. Benchmark algorithms on random high input arrays ***VERY LONG RUNTIME!!***")
    print("3. Benchmark algorithms on ordered arrays ascending")
    print("4. Benchmark algorithms on ordered arrays descending")
    print("5. Benchmark algorithms on random normally distributed arrays")
    choice = input("Choice: ")
    if choice == "1":
        z = 1
        ars = ars1
        sort(ars, z)
    elif choice == "2":
        z = 2
        ars = ars2
        sort(ars, z)
    elif choice == "3":
        z = 3
        ars = ars3
        sort(ars, z)
    elif choice == "4":
        z = 4
        ars = ars3
        sort(ars, z)
    elif choice == "5":
        z = 5
        ars = ars3
        sort(ars, z)
    else:
        print('invalid entry! Try again!')
        choose()

# main() function
def main():
    while True:
        display_menu()
        choice = input("Choice: ")	
        if choice == "1":
            choose()       
        if choice == "2":
            view_averages()        
        if choice == "3":
            plots.choice()
        if choice == "4":
            view_full_results()           
        if choice == "x":
            break
        else:
            print("")

# display menu
def display_menu():
    print("\n==================")
    print("Sorting Algorithms")
    print("==================")
    print("----")
    print("MENU")
    print("----")
    print("1 - Benchmark algorithms")
    print("2 - View table of pre-saved results")
    print("3 - View plots of pre-saved results")
    print("4 - View full results of last test - **long list**")
    print("x - Exit application")

if __name__ == "__main__":
    main()