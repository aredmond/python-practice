import requests
from bs4 import BeautifulSoup
from pprint import pprint as pp

class my_custom_scraper:
    def __init__(self, URL):
        self.page = requests.get(URL)
        self.soup = BeautifulSoup(self.page.text, 'html.parser')

    def make_dict_of_table_r2(self):
        """Scrape site with tables with 2 columns
        """
        tables = self.soup.find_all('table')
        column_count = 0
        tables_dict = {}
        table_count = 0
        for table in tables:
            rows = table.find_all('tr')
            table_name = 'table' + str(table_count)
            tables_dict[table_name] = {}
            for row in rows:
                if row.th:
                    column_count = int(row.th.get('colspan')) if row.th.has_attr('colspan') else None
                    tables_dict[table_name] = {'header_text': row.get_text()}
                else:
                    tables_dict[table_name].update((lambda x: {x[0]:x[1]})([x.get_text() for x in row.find_all('td')]))
            table_count += 1
        return tables_dict

    def make_dict_of_table(self):
        """Scrape site with tables with 2 columns
        """
        tables = self.soup.find_all('table')
        column_count = 0
        tables_dict = {}
        table_count = 0
        for table in tables:
            rows = table.find_all('tr')
            table_name = 'table' + str(table_count)
            tables_dict[table_name] = {}
            tables_dict[table_name]['table_rows'] = []
            table_info = []
            for row in rows:
                if row.th:
                    column_count = int(row.th.get('colspan')) if row.th.has_attr('colspan') else None
                    tables_dict[table_name] = {'header_text': row.get_text()}
                else:
                    table_info_block = []
                    for column in row.find_all('td'):
                        table_info_block.append(column.get_text())
                        # tables_dict[table_name].update((lambda x: {x[0]:x[1]})([x.get_text() for x in row.find_all('td')]))
                    if 'table_rows' in tables_dict[table_name]:
                        tables_dict[table_name]['table_rows'].append(table_info_block)
                    else:
                        tables_dict[table_name]['table_rows'] = [table_info_block]
            table_count += 1
        return tables_dict

mcs = my_custom_scraper('http://toscrape.com/')
pp(mcs.make_dict_of_table())

            
