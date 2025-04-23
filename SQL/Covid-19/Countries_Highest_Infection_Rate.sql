-- This query identifies countries with the highest percentage of their population infected

SELECT
location,
population,
MAX(total_cases) AS HighestInfectionCount,
MAX((total_cases / population)) * 100 AS PercentPopulationInfected
FROM
PortfolioProject..covidDeaths
GROUP BY
location,
population
ORDER BY
PercentPopulationInfected DESC