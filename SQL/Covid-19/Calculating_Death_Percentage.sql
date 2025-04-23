-- This calculates the percentage of deaths relative to total cases. 

SELECT
location,
date,
total_cases,
total_deaths,
(total_deaths / total_cases) * 100 AS DeathPercentage
FROM
PortfolioProject..covidDeaths
ORDER BY
1,
2
