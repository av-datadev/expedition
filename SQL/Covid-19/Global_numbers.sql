-- This calculates the global death percentage

SELECT
SUM(new_cases) as total_cases,
SUM(cast(new_deaths as int)) as total_deaths,
SUM(cast(new_deaths as int)) / SUM(New_Cases) * 100 as DeathPercentage
FROM
PortfolioProject..covidDeaths
WHERE
continent is not null
ORDER BY
1,
2