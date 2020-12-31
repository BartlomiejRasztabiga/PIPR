import random
import matplotlib.pyplot as plt


def main():
    n_samples = 100
    uniform_data = [random.uniform(-3, 3) for _ in range(n_samples)]
    gauss_data = [random.gauss(2, 3) for _ in range(n_samples)]

    fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

    n_bins = 20

    # We can set the number of bins with the `bins` kwarg
    axs[0].hist(uniform_data, bins=n_bins)
    plt.show()

if __name__ == '__main__':
    main()
