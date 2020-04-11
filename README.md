# COVID-19 Cases

A python script that generates latest data set of COVID-19 cases around the globe.

## Setup

```
pip install COVID-19-Cases
```

## Usage

### Import the module.

```
import covid19cases as covid
```

## Fetching of data

### Get the latest cases around the globe.

```
get_global_cases()
```

### Get the latest cases of all affected countries if there's no parameter passed to the method. Else, it will fetch data of specific country.

```
get_country_cases()
get_country_cases("Philippines")
```

### Get the latest cases of all affected continents if there's no parameter passed to the method. Else, it will fetch data of specific continent.

```
get_continent_cases()
get_continent_cases("Asia")
```

## Source

I get the data on this site https://www.worldometers.info/coronavirus/ via Web scraping.

## Note

The keys or format of the dictionary will depend on the website where I scraped the data so it will change from time to time.
