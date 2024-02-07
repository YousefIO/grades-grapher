import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
from scipy.stats import norm

full_marks = [1, 800, 850, 950, 950, 1000, 1800, 6350]

def plot_grades_distribution(csv_files, output_folder, student_id=None):
    # Iterate over the years
    for year in range(1, 9):
        # Create a figure and axes
        fig, ax = plt.subplots()

        # Iterate over the CSV files
        for file_index, csv_file in enumerate(csv_files):
            # Read the data from the CSV file
            data = pd.read_csv(csv_file, header=None)

            # Extract the grades for the current year
            grades = pd.to_numeric(data.iloc[:, year - 1], errors='coerce')

            # Calculate scores as a percentage of full marks
            grades = (grades / full_marks[year - 1]) * 100

            # Ignore zeros and missing values
            grades = grades[grades != 0]
            grades = grades.dropna()

            # Plot the histogram for the current year
            ax.hist(grades, bins=20, density=True, alpha=0.6, label=f'{os.path.basename(csv_file).split(".")[0]}')

            # Fit a normal distribution to the grades
            mu, std = norm.fit(grades)

            # Plot the normal distribution curve
            xmin, xmax = plt.xlim()
            x = np.linspace(xmin, xmax, 100)
            p = norm.pdf(x, mu, std)
            plt.plot(x, p, ["red", "black"][file_index], linewidth=2, label=f'Normal Distribution {os.path.basename(csv_file).split(".")[0]}')

        # Set the title, labels, and legend
        ax.set_title(f'Grades Distribution for Year {year}')
        ax.set_xlabel('Grades (Percentage)')
        ax.set_ylabel('Frequency')
        ax.legend()

        # Save the plot
        plt.savefig(os.path.join(output_folder, f'grades_distribution_year_{year-1}.png'))

plot_grades_distribution(["2017.csv", "2016.csv"], "graphs_folder")