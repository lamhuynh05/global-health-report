# Health Metrics Report

## Introduction: 

This individual analysis part uses the dataset called “SDG Goal 3” that was cleaned and composed by Alan Fekete. This dataset was originally a data file response to a data-request which contains many different sources from multinational government agencies. The cleaned dataset focuses on the global-level health metrics related to United Nations’ Sustainable Development Goal 3 which promotes well-being for everyone across the globe. These are the specific attributes used in this part: Year, Region, Maternal mortality ratio, Adolescent birth rate, Health worker density (NURSEMIDWIFE), Health worker density (PHYSICIAN), Fraction of deaths due to cancer, among deaths due to other diseases, Suicide mortality rate (BOTHSEX), Death rate due to road traffic injuries (BOTHSEX), Mortality rate attributed to different diseases (BOTHSEX), Universal health coverage (UHC) service coverage index. 

## Grouped-Aggregate Summaries: 
### Grouping based on nominal attribute: 

<img width="772" alt="Screenshot 2024-11-22 at 1 40 20 am" src="https://github.com/user-attachments/assets/149a19ba-48b4-4c25-964f-320f5268ee02">

### Grouping based on binned quantitative attribute:

<img width="777" alt="Screenshot 2024-11-22 at 1 41 05 am" src="https://github.com/user-attachments/assets/9bb892bf-9f75-469a-b799-af148a891ab5">

## Charts Production and Evaluation:
### Bar Chart: Fraction of deaths due to cancer among other diseases by Year and Region

In the dataset, the fraction of deaths due to cancer among other diseases were scattered across different regions and years, therefore, a comparative bar chart was chosen to assess the difference in cancer deaths. Data was manipulated using Pandas library and Matplotlib was utilised for visualisation in the creation process of this bar chart. 

<img width="753" alt="Screenshot 2024-11-22 at 1 42 05 am" src="https://github.com/user-attachments/assets/3146ffea-1d6b-415b-a981-b98ded81bc37">

The bar chart is extremely effective as it categorises all of the cancer deaths into specific regions and years, making them readable and ready for further trend comparison and analysis. Looking at this bar chart, one can easily see the regions with the highest or lowest fraction of cancer deaths in certain years because the bars are colour-coded and the bars are next to each other. Separate bar charts standing next to each other make them easier to compare than stacked bar charts because they all have the same starting point. If more data were to be incorporated, this bar chart would still perform well, however it might need more sub-categorisations.

### Scatterplot: Mortality rate from diseases vs UHC service index, coloured by Health Worker Density

This scatterplot was manually created in order to observe the relationship between mortality rate from different diseases and UHC service index. The third variable added is health worker density (physican) and it is shown through the colours of the data points. Similar to the bar chart, pandas library was used to manipulate data and Matplotlib was employed to visualise the scatterplot.

<img width="706" alt="Screenshot 2024-11-22 at 1 43 51 am" src="https://github.com/user-attachments/assets/bf4a80a9-1cfb-4b9c-aa0b-bae2d0ddab3e">

This scatterplot has served its purpose in displaying the visual correlation between the mortality rate of different diseases and UHC service index with the health workers density of physicians as the colour. Based on this scatterplot, we can see that there is a negative correlation between the two main variables. Additionally, the usage of the colour gradient for the data points as well as the colour bar further enhances the usefulness of this scatterplot, making it more informative. If additional data were to be incorporated, the scatterplot would still perform well as scatterplots are made for large datasets, however details such as zoom or hover would be needed to help with visualisation. 

### Bubble Chart: Death Rate due to Road traffic injuries vs Suicide mortality rate, size by Health worker density (PHYSICIANS), colour by Regions

In order to display all four attributes in one chart, bubble chart is chosen to show the relationship between death rate due to road traffic injuries, suicide mortality rate, health worker density (physicians) and regions.

<img width="749" alt="Screenshot 2024-11-22 at 1 47 50 am" src="https://github.com/user-attachments/assets/837c610f-533e-4ca4-b468-8a39919f99cd">

The bubble chart is an excellent method to use when displaying four attributes as one can clearly see the relationship of all four attributes. However, there are still many overlaps between the different sizing of bubbles. The distinct colours help to differentiate between different regions in the chart while the colour legend is clear and easy to read. The legend for bubble sizes shows the certain sizes so viewers can interpret the health worker density corresponds to specific regions. Additionally, because the bubbles are set to 60% opaque, allowing the overlapped bubbles to still be visible. If additional data are incorporated, the bubble chart would not do well as there would be increased overlaps of bubbles and would cause many clusters. 
