#!/usr/bin/python

import requests, json, re, datetime

base_url = "https://search-devero-logstash-logs-o66i5giakedqco7pd4i5q5kigi.us-west-2.es.amazonaws.com:443/"
prefix = 'logstash-'
index_date_format = '%Y.%m.%d'
num_days_to_retain = 14

# Read in the names of all indices from elasticsearch
response = requests.get(base_url +'_cat/indices?format=json')
data = json.loads(response.text)

# For each elasticsearch index
for d in data:
    index_name = d['index']
    # If the name of this index matches our regex
    index_name_parts = re.split(prefix, index_name)
    if len(index_name_parts) == 2:
        # Parse out the date portion of the index name
        index_date_str = index_name_parts[1]
        index_date = datetime.datetime.strptime(index_date_str, index_date_format)
        # If this index is older than num_days_to_retain
        if index_date < datetime.datetime.now() - datetime.timedelta(days=num_days_to_retain):
            # Delete the index
            print 'Deleting index: %s' % index_name
            delete_response = requests.delete(base_url + index_name)
print("DONE")