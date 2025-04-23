-- joining two tables deaths and vaccine

SELECT
dea.continent,
dea.location,
dea.date,
dea.population,
vac.new_vaccinations
FROM
PortfolioProject..covidDeaths dea
JOIN PortfolioProject..covidVaccinations vac ON dea.location = vac.location
and dea.date = vac.date
WHERE
dea.continent is not null
ORDER BY
2,
3