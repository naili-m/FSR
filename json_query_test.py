from ansible_collections.community.general.plugins.filter.json_query import FilterModule

filter_module = FilterModule()
json_query = filter_module.filters()['json_query']

data = {
    "users": [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35}
    ]
}

result = json_query(data, 'users[*].name')
print(f"All names: {result}")
