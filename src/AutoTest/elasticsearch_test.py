from elasticsearch_dsl.connections import connections

try:
    # connections.create_connection(hosts=['http://elasticsearch:9200'])
    connections.create_connection(hosts=['http://localhost:9200/'])

    print("Connected to Elasticsearch!")
except Exception as e:
    print(f"Elasticsearch connection failed: {e}")