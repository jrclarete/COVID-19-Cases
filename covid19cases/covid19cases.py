from bs4 import BeautifulSoup
import requests


global_cases = {}
country_cases = []
th_row = []
table_dict = {}


def load_data():
    """
    Getting the data from https://www.worldometers.info/coronavirus/ via web scraping.
    """
    source = requests.get("https://www.worldometers.info/coronavirus/").text
    soup = BeautifulSoup(source, "lxml")

    # Getting the data of global cases and then added to global_cases dictionary
    for cases in soup.find_all("div", id="maincounter-wrap"):
        global_cases_txt = cases.h1.text.strip(":")
        global_cases_ctr_txt = cases.span.text.strip()
        if(cases.h1.text == "Coronavirus Cases:"):
            global_cases_txt = "Cases"
        global_cases[global_cases_txt] = global_cases_ctr_txt

    # Getting the data of contry cases and then added to country_cases list of dictionary
    table = soup.table
    table_rows = table.find_all("tr")
    for tr in table_rows:
        th = tr.find_all("th")
        td = tr.find_all("td")
        if th:
            for i in th:
                th_text = i.text.replace(u'\xa0', u' ')
                if th_text == "Country,Other":
                    th_text = "Country"
                if th_text == "Serious,Critical":
                    th_text = "Critical"
                if th_text == "Tot Cases/1M pop":
                    th_text = "CasesPerOneMillion"
                if th_text == "Tot Deaths/1M pop":
                    th_text = "DeathsPerOneMillion"
                th_row.append(th_text)
        if td:
            td_row = [j.text.strip() for j in td]
            table_dict = dict(zip(th_row, td_row))
            country_cases.append(table_dict)


def get_global_cases():
    """
    Returns a dictionary of global cases 
    """
    return global_cases


def get_country_cases(country=None):
    """
    Returns a dictionary for sepecific country or list of dictionary for all coutries.

    Parameter:
    country =  Name of a Country that has COVID-19 case. Will return None if country is not available.
    """
    result = None
    if country:
        if country != "Total":
            for search in country_cases:
                if search["Country"].upper() == country.upper():
                    result = search
        return result
    else:
        return country_cases


if __name__ == "__main__":
    load_data()
    print(get_global_cases())
else:
    load_data()
