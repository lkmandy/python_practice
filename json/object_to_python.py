import json


def object_to_json():
    # a Python object (dict):
    my_dict = {
        "first": "Python",
        "second": "Flutter",
        "third": "C",
        "fourth": "Shell Scripting",
        "fifth": "Ruby"
    }

    # convert to json
    json_url = json.dumps(my_dict)

    print(json_url)
