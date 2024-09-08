from load_csv import load
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def convert_population(value):
    """Convert population string with 'M' suffix to numeric value."""
    if isinstance(value, str) and 'M' in value:
        return float(value.replace('M', '').strip())
    return float(value)


def aff_pop(country_name: str):
    """ Plot and compare population of Germany and given country """
    data = load('population_total.csv')

    data_filtered = data[data['country'].isin([country_name, 'Germany'])]
    data_filtered = data_filtered.set_index('country').T.reset_index()
    data_filtered.columns = ['Year', 'Germany', country_name]

    data_long = pd.melt(data_filtered,
                        id_vars=['Year'],
                        value_vars=['Germany', country_name],
                        var_name='Country', value_name='Population')
    data_long['Population'] = data_long['Population'].apply(convert_population)
    data_long['Year'] = data_long['Year'].astype(int)
    data_long = data_long[data_long['Year'] <= 2050]

    print(data_long)

    plt.figure(figsize=(10, 8))
    sns.lineplot(data=data_long, x='Year',
                 y='Population',
                 hue='Country',
                 palette={'Germany': 'green', country_name: 'dodgerblue'})
    plt.legend(loc='lower right')
    plt.title("Population Projections")
    plt.xticks([1800, 1840, 1880, 1920, 1960, 2000, 2040])
    plt.yticks([20, 40, 60, 80, 100], ['20M', '40M', '60M', '80M', '100M'])

    plt.show()


def main():
    aff_pop("Turkey")


if __name__ == '__main__':
    main()
