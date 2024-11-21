import pandas as pd
file_path = 'SDG_goal3_clean.csv'
data = pd.read_csv(file_path)

# Table 1: Average Maternal Mortality Ratio grouped by region
avg_maternal_mortality_by_region = data.groupby('Region').agg(
    Avg_Maternal_Mortality_Ratio=('Maternal mortality ratio', 'mean')
)
# Adding a total row for Table 1
total_row_maternal = pd.DataFrame(avg_maternal_mortality_by_region.mean()).T
total_row_maternal.index = ['Total']
avg_maternal_mortality_with_total = pd.concat([avg_maternal_mortality_by_region, total_row_maternal])

# Display Table 1
print("Average Maternal Mortality Ratio by Region")
print(avg_maternal_mortality_with_total)

# Table 2: Average Health Worker Density binned by Adolescent Birth Rate
# Use pd.qcut for equal-frequency binning (quartiles)
data['Adolescent_Birth_Rate_Binned'] = pd.qcut(data['Adolescent birth rate (per 1,000 women aged 15-19 years)'], q=4)

# Group by binned adolescent birth rate and calculate the average health worker density
avg_health_worker_by_birth_rate = data.groupby('Adolescent_Birth_Rate_Binned').agg(
    Avg_Health_Worker_Density=('Health worker density, by type of occupation (per 10,000 population)::NURSEMIDWIFE', 'mean')
)

# Adding a total row for Table 2
total_row_health_worker = pd.DataFrame(avg_health_worker_by_birth_rate.mean()).T
total_row_health_worker.index = ['Total']
avg_health_worker_with_total = pd.concat([avg_health_worker_by_birth_rate, total_row_health_worker])

# Display Table 2
print("\nAverage Health Worker Density by Adolescent Birth Rate")
print(avg_health_worker_with_total)

