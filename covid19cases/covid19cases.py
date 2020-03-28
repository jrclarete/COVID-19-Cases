from bs4 import BeautifulSoup
import requests
import re


global_cases = {}
country_cases = []
th_row = []
table_dict = {}


def get_match(text):
    """
    Return text found in the list. It will be used for formatting the dictionary keys
    """
    search_text = ""
    key_list = ["Country", "Critical", "Cases/", "Deaths/", "1st"]
    for i in key_list:
        search = re.search(i, text)
        if search:
            search_text = i
            break
    return search_text


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
                th_text = i.text
                if get_match(th_text) == "Country":
                    th_row.append("Country")
                elif get_match(th_text) == "Critical":
                    th_row.append("Critical")
                elif get_match(th_text) == "Cases/":
                    th_row.append("CasesPerOneMillion")
                elif get_match(th_text) == "Deaths/":
                    th_row.append("DeathsPerOneMillion")
                elif get_match(th_text) == "1st":
                    th_row.append("FirstCase")
                else:
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
    Returns a dictionary for sepecific country or list of dictionaries for all coutries.

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


def get_total_cases():
    """
    Returns a dictionary of more informative total cases.
    """
    result = None
    for search in country_cases:
        if search["Country"] == "Total:":
            result = search
    return result


if __name__ == "__main__":
    load_data()
    print(get_global_cases())
else:
    load_data()
