-- selecting the data for analysis

SELECT
location,
date,
total_cases,
new_cases,
total_deaths,
population
FROM
PortfolioProject..covidDeaths
ORDER BY
1,
2