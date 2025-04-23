-- This creates a view named PercentPopulationVaccinated to store the vaccination data.

CREATE VIEW
PercentPopulationVaccinated as
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