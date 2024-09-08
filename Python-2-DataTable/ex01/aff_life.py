import seaborn as sns
import matplotlib.pyplot as plt
from load_csv import load


def aff_life(country_name: str):
    """Plot life expectancy for a given country."""
    data = load("life_expectancy_years.csv")

    if data is None:
        print("Failed to load data.")
        return

    if country_name not in data['country'].values:
        print(f"Country '{country_name}' not found in the dataset.")
        return

    country_data = data[data['country'] == country_name].set_index('country').T
    country_data.reset_index(inplace=True)
    country_data.columns = ['Year', 'Life expectancy']
    country_data['Year'] = country_data['Year'].astype(int)

    plt.figure(figsize=(10, 8))
    sns.lineplot(data=country_data, x='Year', y='Life expectancy')
    plt.title(f"{country_name} Life expentancy Projections")
    plt.xticks([1800, 1840, 1880, 1920, 1960, 2000, 2040, 2080])
    plt.show()


def main():
    aff_life("Germany")


if __name__ == '__main__':
    main()
