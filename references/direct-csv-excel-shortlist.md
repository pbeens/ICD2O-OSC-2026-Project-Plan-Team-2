# Direct CSV/Excel Shortlist (No ZIP)

Verified on 2026-03-11 using Open Canada CKAN API (`package_show`) resource links.

Selection rule:
- Direct `.csv` or `.xlsx` URL
- English/French pair available
- Beginner-friendly import path (`pd.read_csv(url)` or `pd.read_excel(url)`)

## 1) Temperature Change in Canada (Seasonal)
- Dataset page: https://open.canada.ca/data/en/dataset/00f5bde8-fac4-431f-a0df-3ed0bf21e1dc
- English CSV: https://www.canada.ca/content/dam/eccc/documents/csv/cesindicators/temperature-change/2019/Temperature-change-seasonal-en.csv
- French CSV: https://www.canada.ca/content/dam/eccc/documents/csv/cesindicators/temperature-change/2019/Temperature-change-seasonal-fr.csv
- Why it fits Grade 10: simple time-series and trendline charts.

## 2) Extreme Heat Events
- Dataset page: https://open.canada.ca/data/en/dataset/2cc1ad59-97cf-4652-839a-7cfaa943ebcf
- English CSV: https://www.canada.ca/content/dam/eccc/documents/csv/cesindicators/extreme-heat-events/2025/cumulative-days-summary.csv
- French CSV: https://www.canada.ca/content/dam/eccc/documents/csv/cesindicators/extreme-heat-events/2025/cumulatif-jours-sommaire.csv
- Why it fits Grade 10: clear annual trend and climate relevance.

## 3) Greenhouse Gas Emissions Projections
- Dataset page: https://open.canada.ca/data/en/dataset/2ff017d8-e122-4d6b-a394-f919b64018cc
- English CSV: https://www.canada.ca/content/dam/eccc/documents/csv/cesindicators/ghg-projections/2025/ghg-emissions-projections-en.csv
- French CSV: https://www.canada.ca/content/dam/eccc/documents/csv/cesindicators/ghg-projections/2025/projections-emissions-ges-fr.csv
- Why it fits Grade 10: historical + projected values for regression and forecasting discussion.

## 4) Water Quantity at Monitoring Stations
- Dataset page: https://open.canada.ca/data/en/dataset/2a5c1689-c2f4-418c-adb8-a21fd67982fd
- English CSV: https://indicators-map.canada.ca/CSVs/en/Water%20quantity%20at%20monitoring%20stations.csv
- French CSV: https://indicators-map.canada.ca/CSVs/fr/Quantit%C3%A9%20deau%20dans%20les%20stations%20de%20suivi.csv
- Why it fits Grade 10: many rows for filtering by province/region and scatter/bar chart tasks.

## 5) Precipitation Change in Canada
- Dataset page: https://open.canada.ca/data/en/dataset/38145e6c-4184-43b1-afe1-c668a98ab56e
- English CSV: https://www.canada.ca/content/dam/eccc/migration/main/indicateurs-indicators/acd78526-759a-411a-a950-7372ab711c0e/precipitationchange_en.csv
- French CSV: https://www.canada.ca/content/dam/eccc/migration/main/indicateurs-indicators/acd78526-759a-411a-a950-7372ab711c0e/precipitationchange_fr.csv
- Why it fits Grade 10: concise dataset for quick visualizations and slope interpretation.

## 6) Air Quality (Pick One English/French Pair)
- Dataset page: https://open.canada.ca/data/en/dataset/01313060-f926-4460-a537-4204e47c88a5
- English CSV (national indexed series): https://www.canada.ca/content/dam/eccc/documents/csv/cesindicators/air-quality/2026/EN/1-national-indexed-2026-en.csv
- French CSV (national indexed series): https://www.canada.ca/content/dam/eccc/documents/csv/cesindicators/air-quality/2026/fr/1-national-indexe-2026-fr.csv
- Why it fits Grade 10: straightforward line charts and provincial/regional comparison extensions.

## Suggested First Notebook
Start with dataset #2 (Extreme Heat Events) or #1 (Temperature Change):
- Minimal preprocessing
- Direct CSV imports
- Immediate charting with Plotly Express
