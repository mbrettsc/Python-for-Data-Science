from load_csv import load

dataset = load("life_expectancy_years.csv")


if dataset is not None:
    print(dataset.head())
