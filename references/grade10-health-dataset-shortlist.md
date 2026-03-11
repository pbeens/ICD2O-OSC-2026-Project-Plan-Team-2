# Grade 10 Health Dataset Shortlist

Potential datasets from Open Canada shared on 2026-03-11.

## Recommended First Pick
**Selection rule for core notebooks:** direct `.csv` or `.xlsx` links only (no ZIP handling).

Use this rule for beginner-friendly analysis:
- One-step `pd.read_csv(url)` or `pd.read_excel(url)`
- No archive extraction logic
- No spatial/geospatial loaders required

## Advanced Option (Optional)
**Youth Health Indicators (age 1-17)**  
Link: https://open.canada.ca/data/dataset/4a21b975-f05d-4230-a372-9ca9bd5b8af1  
Reason: currently provided as ZIP (`13100947-eng.zip`), which adds extra loading steps.

## Candidate List
1. Youth Health Indicators (age 1-17)  
   https://open.canada.ca/data/dataset/4a21b975-f05d-4230-a372-9ca9bd5b8af1
2. Youth Health Indicators by Income and Parental Education  
   https://open.canada.ca/data/en/dataset/900c8050-0fb5-4e9b-bc2b-6dc1a24c9f36
3. Health Characteristics of Children and Youth (Canadian Health Survey)  
   https://open.canada.ca/data/dataset/58aa2d75-ff59-4a8e-91cc-70d4765e307f
4. Youth Health Changes (2019-2023)  
   https://open.canada.ca/data/en/dataset/ef44c64a-6f75-443b-a691-28d232c14587
5. Functional Difficulties Among Youth  
   https://open.canada.ca/data/en/dataset/0a56b176-1878-40fb-ae2c-41b11ada89eb
6. Health Indicators (Canada and Provinces)  
   https://open.canada.ca/data/en/dataset/07bf1adb-c6a5-4e91-8911-5565f4e38e0f

## Next Action
For each selected dataset, capture both direct resource links:
- English CSV download URL
- French CSV download URL

Only move to notebook creation when at least one direct CSV/Excel resource URL is confirmed.
