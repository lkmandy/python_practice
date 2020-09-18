import json


def json_to_object():
    # sample json code snippet. Must be a byte, string or bytearray
    json_url = '''{"employees":[  
        {"name":"Shyam", "email":"shyamjaiswal@gmail.com"},  
        {"name":"Bob", "email":"bob32@gmail.com"},  
        {"name":"Jai", "email":"jai87@gmail.com"}  
    ]}'''

    # convert to object
    destination = json.loads(json_url)
    print(destination)
