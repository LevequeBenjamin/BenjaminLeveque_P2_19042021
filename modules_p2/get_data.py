# import libraries
import requests
from bs4 import BeautifulSoup


# query the website and return the html to the variable 'res'
# parse the html using beautiful soup and store in variable 'soup'
def get_data(url: str) -> BeautifulSoup:
    """[From a url, return a data structure representing a parsed HTML or XML document]

    Args:
        url (str): [A url]

    Returns:
        BeautifulSoup: [A data structure representing a parsed HTML or XML document]
    """
    try:
        res = requests.get(url, timeout=3)
        if res.ok:
            soup = BeautifulSoup(res.content, 'html.parser')
            return soup
        res.raise_for_status()
    except requests.exceptions.HTTPError as err_http:
        print("Http Error:", err_http)
    except requests.exceptions.ConnectionError as err_connect:
        print("Error Connecting:", err_connect)
    except requests.exceptions.Timeout as err_timeout:
        print("Timeout Error:", err_timeout)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)


