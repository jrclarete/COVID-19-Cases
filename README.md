# COVID-19 Cases

A python script that generates latest data set of COVID-19 cases around the globe.

## Setup

```
pip install COVID-19-Cases
```

## Usage

The script will return a dictionary for the Global and Total cases and/or list of dictionaries for the Country cases

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
[{'Country': 'USA', 'TotalCases': '104,256', 'NewCases': '+130', 'TotalDeaths': '1,704', 'NewDeaths': '+8', 'TotalRecovered': '2,525', 'ActiveCases': '100,027', 'Critical': '2,494', 'CasesPerOneMillion': '315', 'DeathsPerOneMillion': '5', 'FirstCase': 'Jan 20'}, {'Country': 'Italy', 'TotalCases': '86,498', 'NewCases': '', 'TotalDeaths': '9,134', 'NewDeaths': '', 'TotalRecovered': '10,950', 'ActiveCases': '66,414', 'Critical': '3,732', 'CasesPerOneMillion': '1,431', 'DeathsPerOneMillion': '151', 'FirstCase': 'Jan 29'}]
```

```
# Get the latest case of specific country
print(get_country_cases("USA"))

Sample output:
{'Country': 'USA', 'TotalCases': '104,256', 'NewCases': '+130', 'TotalDeaths': '1,704', 'NewDeaths': '+8', 'TotalRecovered': '2,525', 'ActiveCases': '100,027', 'Critical': '2,494', 'CasesPerOneMillion': '315', 'DeathsPerOneMillion': '5', 'FirstCase': 'Jan 20'}
```

```
# Get the total data in more informative way
print(get_total_cases())

Sample output:
{'Country': 'Total:', 'TotalCases': '613,828', 'NewCases': '+17,516', 'TotalDeaths': '28,229', 'NewDeaths': '+888', 'TotalRecovered': '137,223', 'ActiveCases': '448,376', 'Critical': '23,995', 'CasesPerOneMillion': '78.7', 'DeathsPerOneMillion': '3.6', 'FirstCase': ''}
```

The data will change from time to time.

## Source

I get the data on this site https://www.worldometers.info/coronavirus/ via Web scraping.
