import numpy as np
import matplotlib.pyplot as plt

# Plot behavioral response from 10 seconds before addition of stimulus to 60 seconds after addition with the curve
# fit to the data. Takes a dataframe with the behavior data (proportion of 2 week old and 2 month old ants
# outside the nest at timepoints -60 to 60), a dataframe with the curve fit to the data (using GraphPad Prism) and
# outputs figure to a png file.

def timecourse_alarm(df, curve_df, output_file):
    y_variable_2wo = 'prop_outside_2wo'
    y_variable_2mo = 'prop_outside_2mo'
    mean_2wo = df.groupby('time')[y_variable_2wo].mean()
    mean_2mo = df.groupby('time')[y_variable_2mo].mean()
    std_2wo = df.groupby('time')[y_variable_2wo].std()
    std_2mo = df.groupby('time')[y_variable_2mo].std()
    sample_size_2wo = df.groupby('time')[y_variable_2wo].count()
    sample_size_2mo = df.groupby('time')[y_variable_2mo].count()
    sem_2wo = std_2wo / np.sqrt(sample_size_2wo)
    sem_2mo = std_2mo / np.sqrt(sample_size_2mo)

    # Convert index and values to NumPy arrays
    mean_2wo_index = mean_2wo.index.to_numpy()
    mean_2mo_index = mean_2mo.index.to_numpy()
    mean_2wo_values = mean_2wo.to_numpy()
    mean_2mo_values = mean_2mo.to_numpy()

    # pull out appropriate data from curve_df and convert to numpy arrays
    curve_2wo_mean = (curve_df['mean_2wo']).to_numpy()
    curve_2mo_mean = (curve_df['mean_2mo']).to_numpy()
    time = (curve_df['time']).to_numpy()
    curve_2wo_CIhigh = (curve_df['CIhigh_2wo']).to_numpy()
    curve_2mo_CIhigh = (curve_df['CIhigh_2mo']).to_numpy()
    curve_2wo_CIlow = (curve_df['CIlow_2wo']).to_numpy()
    curve_2mo_CIlow = (curve_df['CIlow_2mo']).to_numpy()


    # Plotting the mean and 95% CI
    plt.figure(figsize=(6, 4))
    plt.figure(facecolor='white')
    #plt.scatter(mean_2wo_index, mean_2wo_values, label='2 week old', color='#66C2A7', s=50)
    #plt.scatter(mean_2mo_index, mean_2mo_values, label='2 month old', color='#FC8D62', s=50)
    plt.errorbar(mean_2wo_index, mean_2wo_values, label='2 week old', yerr=sem_2wo, fmt='o', color='#66C2A7', alpha=1, elinewidth=4, markersize=14)
    plt.errorbar(mean_2mo_index, mean_2mo_values, label='2 month old', yerr=sem_2mo, fmt='o', color='#FC8D62', alpha=1, elinewidth=4, markersize=14)
    plt.plot(time, curve_2wo_mean, label='2 week old', color='#66C2A7', alpha=0.3)
    plt.plot(time, curve_2mo_mean, label='2 month old', color='#FC8D62', alpha=0.3)
    plt.fill_between(time, curve_2wo_mean + curve_2wo_CIhigh, curve_2wo_mean - curve_2wo_CIlow, alpha=0.3, color='#66C2A7')
    plt.fill_between(time, curve_2mo_mean + curve_2mo_CIhigh, curve_2mo_mean - curve_2mo_CIlow, alpha=0.3, color='#FC8D62')
    plt.tick_params(axis='both', labelsize=12, color='black')
    plt.xlabel('Time (seconds)', fontsize=12, color='black')
    plt.ylabel('Proportion of Ants Outside Nest', fontsize=12, color='black')
    plt.ylim(0, 1)
    plt.xlim(-12,62)
    plt.grid(axis='y', color='lightgrey', linestyle='--', linewidth=1)
    plt.savefig(output_file)