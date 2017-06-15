#!/usr/bin/python

# This small script demonstrates making a connection to AWS Hosted Elasticsearch

# You will need to run the following on the command line to install the required libraries for this test:
#   sudo pip install elasticsearch
#   sudo pip install requests-aws4auth

from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
# This is for pretty-printing the es.info() response
import json

access_key = 'ENTER_ACCESS_KEY'
secret_key = 'ENTER_SECRET_KEY'

region = 'us-east-1'
awsauth = AWS4Auth(access_key, secret_key, region, 'es')
host = 'ENTER_DOMAIN_ENDPOINT'

es = Elasticsearch(
    hosts=[{'host': host, 'port': 443}],
    http_auth=awsauth,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
)

print(json.dumps(es.info(), indent=2))
