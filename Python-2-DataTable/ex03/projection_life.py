from load_csv import load
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def projection_life():
    """Plot life expectancy vs GDP for 1900."""
    gdp_data = load(
        'income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
    life_expectancy_data = load('life_expectancy_years.csv')
    gdp_1900 = gdp_data[['country', '1900']
                        ].rename(columns={'1900': 'GDP_1900'})
    life_expectancy_1900 = life_expectancy_data[
        ['country', '1900']].rename(columns={'1900': 'Life_Expectancy_1900'})

    merged_data = pd.merge(gdp_1900, life_expectancy_1900, on='country')
    merged_data.dropna(inplace=True)

    print(merged_data)
    
    plt.figure(figsize=(10, 8))
    sns.scatterplot(merged_data, x='GDP_1900',
                    y='Life_Expectancy_1900', s=80, edgecolor=None)
    plt.title('1900')
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life expectancy')
    plt.xscale('log')
    plt.xticks([300, 1000, 10000], ['300', '1K', '10K'])
    plt.show()



def main():
    projection_life()


if __name__ == '__main__':
    main()
