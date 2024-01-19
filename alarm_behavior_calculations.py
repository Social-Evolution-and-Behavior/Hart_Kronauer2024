import pandas as pd

# Function takes the csv file with raw data, total number of ants, total number of 2 week old ants, and
# total number of 2 month old ants as input and outputs a dataframe with the number of ants outside the nest (total,
# 2 week old, and 2 month old), the number of ants inside the nest (total, 2 week old, and 2 month old), the proportion
# ants outside the nest (total, 2 week old, and 2 month old), and of the ants inside the nest, the proportion of 2 week
# old and 2 month old that leave at each timepoint.

def all_calculations(input_file, n_total, n_2wo, n_2mo, stimulus):
    # Read the CSV file into a pandas DataFrame with the first row as header and the time as the index column
    data_path = '/Users/lindsey/Documents/Kronauer Lab/Alarm Response/olfactorymaturation/raw_data/'
    input_file = data_path + input_file + "_60prepost.csv"
    df = pd.read_csv(input_file, header=[0])

    # Re-name columns for easier processing
    df.rename(columns={'# ants outside nest': 'n_outside_total', '# 2wo outside nest': 'n_outside_2wo',
                       '# 2mo outside nest': 'n_outside_2mo'}, inplace=True)

    # Add info about stimulus
    df["stimulus"] = stimulus

    # Add info about number of ants
    df['n_total'] = n_total
    df['n_2wo'] = n_2wo
    df['n_2mo'] = n_2mo

    # Calculate proportion of ants outside the nest at all timepoints
    df["prop_outside_total"] = df["n_outside_total"] / n_total
    df["prop_outside_2wo"] = df["n_outside_2wo"] / n_2wo
    df["prop_outside_2mo"] = df["n_outside_2mo"] / n_2mo

    return df