import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def calculate_pdf(x_values, mean, std_dev):
    return norm.pdf(x_values, mean, std_dev)

def plot_pdf(x_values, pdf_values):
    plt.plot(x_values, pdf_values, color='b', label='PDF')
    plt.xlabel('Values')
    plt.ylabel('Density')
    plt.title('Probability Density Function (PDF)')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()

def main():
    print("Welcome to the PDF Calculator!")
    mean = float(input("Enter the mean of the normal distribution: "))
    std_dev = float(input("Enter the standard deviation of the normal distribution: "))
    x_min = float(input("Enter the minimum x value for the plot: "))
    x_max = float(input("Enter the maximum x value for the plot: "))
    num_points = int(input("Enter the number of points for the plot: "))

    x_values = np.linspace(x_min, x_max, num_points)
    pdf_values = calculate_pdf(x_values, mean, std_dev)

    plot_pdf(x_values, pdf_values)

if __name__ == "__main__":
    main()
