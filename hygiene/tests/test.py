from hygiene import Singleton
import json
# Example JSON string
singletons = [
    {"name": "John", "age": 30, "city": "New York"},
    '{"name": "John", "age": 30, "city": "New York"}',
    list({"name": "John", "age": 30, "city": "New York"}),
    [{"name": "John", "age": 30, "city": "New York"}]
]

qdrant_payload_examples = [
    {
        "count": 10,
        "sizes": [35, 36, 38]
    },
    {
        "price": 11.99,
        "ratings": [9.1, 9.2, 9.4]
    },
    {
        "is_delivered": True,
        "responses": [False, False, True, False]
    },
    {
        "name": "Alice",
        "friends": [
            "bob",
            "eva",
            "jack"
        ]
    },
    {
        "location": {
            "lon": 52.5200,
            "lat": 13.4050
        },
        "cities": [
            {
                "lon": 51.5072,
                "lat": 0.1276
            },
            {
                "lon": 40.7128,
                "lat": 74.0060
            }
        ]
    }
]

def calculate_ratio(string, json_obj):
        string_size = len(string.encode('utf-8'))
        json_size = len(json.dumps(json_obj).encode('utf-8'))
        ratio = string_size / json_size
        print(f'JSON->YAML bytes ratio: {ratio}')

boxing = Singleton.boxing()

for each in singletons:
    package = boxing.Payload(data=each, fmt="yml")
    payload = package.deliver()
    print(payload)
    calculate_ratio(payload, each)

for each in qdrant_payload_examples:
    package = boxing.Payload(data=each, fmt="yml")
    payload = package.deliver()
    print(payload)
    calculate_ratio(payload, each)
