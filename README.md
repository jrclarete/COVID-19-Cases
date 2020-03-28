# COVID-19 Cases

A python script that generates latest data set of COVID-19 cases around the globe.

## Setup

```
pip install COVID-19-Cases
```

## Usage

The script will return a dictionary for the Global cases and/or list of dictionary for the Country cases

```
import covid19cases as covid
```

```
# Get the latest cases around the globe
print(covid.get_global_cases())

Sample output:
{'Cases': '590,424', 'Deaths': '26,950', 'Recovered': '132,458'}
```

```
# Get the latest cases of all affected Countries
print(covid.get_country_cases())

Sample output:
[{'Country': 'China', 'TotalCases': '81,340', 'NewCases': '+55', 'TotalDeaths': '3,292', 'NewDeaths': '+5', 'TotalRecovered': '74,588', 'ActiveCases': '3,460', 'Critical': '1,034', 'CasesPerOneMillion': '57', 'DeathsPerOneMillion': '2'}, {'Country': 'USA', 'TotalCases': '100,514', 'NewCases': '+15,079', 'TotalDeaths': '1,546', 'NewDeaths': '+251', 'TotalRecovered': '2,465', 'ActiveCases': '96,503', 'Critical': '2,463', 'CasesPerOneMillion': '304', 'DeathsPerOneMillion': '5'}]
```

```
# Get the latest case of specific country
print(covid.get_country_cases("Italy"))

Sample output:
{'Country': 'Italy', 'TotalCases': '86,498', 'NewCases': '+5,909', 'TotalDeaths': '9,134', 'NewDeaths': '+919', 'TotalRecovered': '10,950', 'ActiveCases': '66,414', 'Critical': '3,732', 'CasesPerOneMillion': '1,431', 'DeathsPerOneMillion': '151'}
```

The data will change from time to time.

## Source

I get the data on this site https://www.worldometers.info/coronavirus/ via Web scraping.
