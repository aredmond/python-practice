from bs4 import BeautifulSoup as bs
import requests as rq
import pickle
import os

URL = "https://www.ec2instances.info"

def pickle_request():
    request_pickle_file = '/tmp/' + 'ec2inforequest.txt'
    if not os.path.isfile(request_pickle_file):
        site_data = rq.get(URL)
        # soup = bs(site_data.text, 'html.parser')
        print('Creating Pickle object and storing to:', request_pickle_file)
        pickle.dump( site_data, open( request_pickle_file, "wb" ))
    else:
        print(request_pickle_file, 'exists, reading and loading pickle data.')
        site_data = pickle.load( open( request_pickle_file, "rb" ))
    return site_data

site_data = pickle_request()
soup = bs(site_data.text, 'html.parser')

table = soup.find('table')
tbody = table.find('tbody')
trs = tbody.find_all('tr')

instances = {}
for tr in trs:
    if hasattr(tr, 'id'):
        instance_id = tr['id']
        instances[instance_id] = {'id': instance_id}
    else:
        print("stuff")
        continue
    for td in tr.find_all('td'):
        td_c = td['class'][0]
        if td_c == 'name':
            instances[instance_id]['name'] = td.content[0]
        elif td_c == 'memory':
            instances[instance_id]['memory'] = td.find('span').contents[0]


print(instances)