-- This creates a temporary table to store and calculate vaccination percentages.

DROP TABLE if exists PercentPopulationVaccinated CREATE TABLE
PercentPopulationVaccinated (
Continent nvarchar(255),
Location nvarchar(255),
Date datetime,
Population numeric,
New_vaccinations numeric,
RollingPeopleVaccinated numeric
)
INSERT INTO
PercentPopulationVaccinated
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
SELECT
*,
(RollingPeopleVaccinated / Population) * 100
FROM
PercentPopulationVaccinated