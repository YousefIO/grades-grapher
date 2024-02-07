import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
from scipy.stats import norm

def plot_grades_distribution(csv_files, output_folder, student_id=None):
    for csv_file in csv_files:
        data = pd.read_csv(csv_file, header=None)
        years_data = data.iloc[:, 1:-1]
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        for year in range(1, 7):
            print(year)
            plt.figure()
            grades = pd.to_numeric(years_data.iloc[:, year - 1], errors='coerce')
            grades = grades[grades != 0]  # Ignore zeros
            grades = grades.dropna()
            plt.hist(grades, bins=20, density=True, alpha=0.6, color='g')
            mu, std = norm.fit(grades)
            xmin, xmax = plt.xlim()
            x = np.linspace(xmin, xmax, 100)
            p = norm.pdf(x, mu, std)
            plt.plot(x, p, 'k', linewidth=2)
            title = f'Year {year} Grades Distribution for {os.path.basename(csv_file)}'
            plt.title(title)
            plt.xlabel('Grades')
            plt.ylabel('Frequency')
            if student_id is not None:
                student_grade = data[data[0] == student_id][year].values[0]
                plt.axvline(x=student_grade, color='r', linestyle='--', label=f'Student {student_id}')
            plt.savefig(os.path.join(output_folder, f'{os.path.splitext(os.path.basename(csv_file))[0]}_Year_{year}_Distribution.png'))
            plt.close()

plot_grades_distribution(["cleaned_2017.csv", "output.csv"], "graphs_folder")
