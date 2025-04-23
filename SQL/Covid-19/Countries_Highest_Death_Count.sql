-- This query identifies countries with the highest total death counts.

SELECT
location,
MAX(cast(total_deaths as int)) AS TotalDeathCount
FROM
PortfolioProject..covidDeaths
WHERE
continent is not null
GROUP BY
location
ORDER BY
TotalDeathCount DESC