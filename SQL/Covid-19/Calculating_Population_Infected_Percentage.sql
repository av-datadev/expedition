-- This calculates the percentage of the population that has been infected

SELECT
location,
date,
total_cases,
population,
(total_cases / population) * 100 AS PercentPopulationInfected
FROM
PortfolioProject..covidDeaths
ORDER BY
1,
2