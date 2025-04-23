-- This uses a CTE (Common Table Expression) to calculate the percentage of the population vaccinated.

WITH
PopvsVac (
Continent,
Location,
Date,
Population,
New_vaccinations,
RollingPeopleVaccinated
) as (
SELECT
dea.continent,
dea.location,
dea.date,
dea.population,
vac.new_vaccinations,
SUM(CONVERT(int, vac.new_vaccinations)) OVER (
PARTITION BY
dea.location
ORDER BY
dea.location,
dea.Date
) AS RollingPeopleVaccinated
FROM
PortfolioProject..covidDeaths dea
JOIN PortfolioProject..covidVaccinations vac ON dea.location = vac.location
and dea.date = vac.date
)
SELECT
*,
(RollingPeopleVaccinated / Population) * 100
FROM
PopvsVac