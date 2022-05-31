import matplotlib.pyplot as plt
import pandas as pd
import benchmarking as bm

# rows from csv table to skip
skip1 = 1
skip2 = [0,4,5,6]
skip3 = [0,2,3]

# titles for various tables
title1 = "Algorithm benchmarking"
title2 = "Algorithm benchmarking Bubble and Insertion Sort"
title3 = "Algorithm benchmarking for Merge, Quick and Bucket Sort"

# function to draw plots
def view_chart(x, title):
    df = pd.read_csv("results/averages.csv", skiprows = x)
    df.rename(columns = {'Array_size':'Algorithm'}, inplace = True)
    df.set_index('Algorithm').T.plot(marker = 'o')
    plt.xlabel("Input size n")
    plt.ylabel("Running time (milliseconds)")
    plt.title(title)
    plt.grid()
    plt.show()

def plot_menu():
    print("\n1. View plot of average benchmarking results")
    print("2. View plot of average benchmarking results for Bubble and Insertion sort")
    print("3. View plot of average benchmarking results for Merge, Quick and Bucket sort")
    print("4. Back to main menu")


def choice():
    plot_menu()
    choice = input("Choice: \n")

    if choice == "1":
        x = skip1
        title=title1
        view_chart(x, title)

    elif choice == "2":
        x = skip2
        title=title2
        view_chart(x, title)

    elif choice == "3":
        x = skip3
        title=title3
        view_chart(x, title)
               
    elif choice == "x":
        bm.display_menu()   
        
    else:
        print("Invalid entry! Try again!")