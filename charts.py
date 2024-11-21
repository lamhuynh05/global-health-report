import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = '/Users/lamhuynh/Desktop/SDG_goal3_clean.csv'
df = pd.read_csv(file_path)

# Ensure 'Region' is treated as a categorical variable
df['Region'] = df['Region'].astype('category')
df['Year'] = df['Year'].astype(int)

# 1. Bar Chart: Fraction of deaths due to cancer by Year and Region
plt.figure(figsize=(10, 6))

# Pivot data for bar plot
cancer_data = df.pivot_table(values='Fraction of deaths due to cancer, among deaths due to cardiovascular disease, cancer, diabetes or chronic respiratory disease', 
                            index='Year', columns='Region', aggfunc='mean')

# Create bar plot for each region
cancer_data.plot(kind='bar', stacked=False, ax=plt.gca())

plt.title('Fraction of Deaths Due to Cancer Among Deaths Due to other Diseases by Year and Region')
plt.ylabel('Fraction of Deaths Due to Cancer, Among Deaths Due to other Diseases')
plt.xlabel('Year')
plt.xticks(rotation=45)
plt.legend(title='Region', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# 2. Scatterplot: Mortality rate from chronic diseases vs UHC service index, colored by Health Worker Density
plt.figure(figsize=(10, 6))

# Data for scatter plot
x = df['Mortality rate attributed to cardiovascular disease, cancer, diabetes or chronic respiratory disease (probability):::BOTHSEX']
y = df['Universal health coverage (UHC) service coverage index']
color = df['Health worker density, by type of occupation (per 10,000 population)::PHYSICIAN']

# Scatter plot
scatter = plt.scatter(x, y, c=color, cmap='coolwarm', alpha=0.7)

# Add color bar for health worker density
plt.colorbar(scatter, label='Health Worker Density (PHYSICIAN)')

# Add labels and title
plt.title('Disease Mortality Rate vs UHC Service Index, Colored by Health Worker Density')
plt.xlabel('Mortality Rate (Cardiovascular, Cancer, Diabetes, Chronic Respiratory) (BOTHSEX)')
plt.ylabel('UHC Service Index')
plt.tight_layout()
plt.show()

# 3. Bubble chart: Death rate due to road traffic injuries vs suicide mortality rate, size by health worker den

# Set up the bubble chart
plt.figure(figsize=(10, 6))
bubble_sizes = np.sqrt(df['Health worker density, by type of occupation (per 10,000 population)::PHYSICIAN']) * 100

# Bubble chart
region_colors = {
    'Africa': 'blue',   
    'Asia': 'green',     
    'Europe': 'orange',   
    'Oceania': 'purple',  
    'Americas': 'red'  
}
scatter = plt.scatter(
    x=df['Death rate due to road traffic injuries, by sex (per 100,000 population):::BOTHSEX'],
    y=df['Suicide mortality rate, by sex (deaths per 100,000 population):::BOTHSEX'],
    s=bubble_sizes,
    c=df['Region'].map(region_colors),  # Map colors using the named colors
    alpha=0.6
)
# Labels and title
plt.title('Death Rate Due to Road Traffic Injuries vs Suicide Mortality Rate, by Health Worker Density (Physician) and Region')
plt.xlabel('Death Rate Due to Road Traffic Injuries (BOTHSEX) (per 100,000 population)')
plt.ylabel('Suicide Mortality Rate (BOTHSEX) (per 100,000 population)')

# Legend for regions (color legend)
for region, color in region_colors.items():
    plt.scatter([], [], c=color, label=region, s=100)  # Add invisible points to create the color legend

# Legend for bubble sizes (size legend based on physician densities)
for size in [5, 10, 20, 50, 75]:  # These values should represent physicians per 10,000 population
    plt.scatter([], [], c='gray', alpha=0.6, s=np.sqrt(size) * 80, label=f'{size} per 10,000')

plt.legend(title="Physicians per 10,000", bbox_to_anchor=(1.05, 0.5), loc='center left', frameon=True, borderpad=2, labelspacing=1.5)

# Display the plot
plt.tight_layout()
plt.show()
