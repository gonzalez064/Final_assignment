# Income and Life Expectancy Analysis in Spanish Provinces

This project analyzes the relationship between **income** and **life expectancy at age 65** across Spanish provinces using publicly available datasets.

## Hypothesis

> Higher income levels are associated with a longer life expectancy at 65.

## Project Structure

.
├── data/
│ ├── life_expectancy.csv
│ └── rent.csv
├── notebooks/
│ └── analysis.ipynb
├── src/
│ ├── analysis.py
├── tests/
│ └── test_analysis.py
├── requirements.txt
└── README.md

## Analysis

The dataset includes income and life expectancy data by province and year.

Data cleaning involves replacing commas, handling missing values, and converting strings to floats.

A correlation coefficient of 0.46 was observed when including the year 2020.

When 2020 is excluded (to remove the COVID-19 effect), the correlation increases to 0.52.

## Testing
Run unit tests with:
pytest tests/

## Results

- Correlation (with 2020): **0.46**
- Correlation (excluding 2020): **0.52**

## Conclusion

There is a moderate positive correlation between income and life expectancy at age 65. The drop in correlation when including 2020 suggests that the pandemic disrupted the usual relationship between economic conditions and longevity. This emphasizes the impact of external shocks like health crises on socioeconomic indicators.

## Data sources
>INE - Life Expectancy

>INE - Income by Province
