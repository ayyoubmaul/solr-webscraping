import pysolr
import requests


# # Establish a connection to Solr
solr = pysolr.SolrCoreAdmin('http://localhost:8983/solr/admin/cores')
# Create a new Solr core
core_name = 'example_core'
schema = [
    {
        "name": "id",
        "type": "string",
        "indexed": True,
        "stored": True,
        "required": True,
        "uniqueKey": True
    },
    {
        "name": "title",
        "type": "text_general",
        "indexed": True,
        "stored": True
    },
    {
        "name": "content",
        "type": "text_general",
        "indexed": True,
        "stored": True
    }
]
solr.create(core_name, schema='/Users/ayyoub/gitrepo/solr-webscraping/schema.xml')
# Define the schema for the core
# solr_url = f'http://localhost:8983/solr/{core_name}/'

# solr = pysolr.Solr(solr_url)

# # Configure the schema for the core
# solr.(core_name, schema)


"""
curl -X POST -H 'Content-type:application/json' --data-binary '@/Users/ayyoub/gitrepo/solr-webscraping/schema.json' http://localhost:8983/solr/example_core/schema
"""

# Add document
"""
[
    {
        "age_range":"3-5 years",
        "sku":"abc0001",
        "created_at":"2022-02-20T00:00:00Z",
        "description":"Some long long long long long and intersting description",
        "category":"toys",
        "rrp":"11.99",
        "quantity":"20000"
    },
    {
        "age_range":"6-8 years",
        "sku":"abc0002",
        "created_at":"2022-02-20T00:00:00Z",
        "description":"short description",
        "category":["books","toys"],
        "rrp":"14.99",
        "quantity":"30000"
    }
]
"""

"""
curl -X POST -H 'Content-Type: application/json' 'http://localhost:8983/solr/example_core/update?commit=true' --data-binary '@/Users/ayyoub/gitrepo/solr-webscraping/data.json'
"""
