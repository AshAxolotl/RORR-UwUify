import json
import os.path
import re

langJson = "lang_from_bui.json"

data = {}

def read_json_data():
    with open(langJson, "r") as file:
        fileContents = file.read()

    data = json.loads(fileContents)

    return data

def write_json_data():
    data_json = json.dumps(data, indent=4)
    with open("uwu-engwish/lang.json", "w") as file:
        file.write(data_json)


def list_or_string(value):
    if isinstance(value, str):
        value = uwuify(value)
    
    if isinstance(value, list):
        for i in range(len(value)):
            value[i] = uwuify(value[i])

    return value

def uwuify(text: str):
    #needs to not replace <l> and <r> enz (PROBLAY using regex?)

    text = text.replace("l", "w")
    text = text.replace("L", "W")
    text = text.replace("r", "w")
    text = text.replace("R", "W")

    return text


if os.path.isfile(langJson):
    data = read_json_data()
    for key in data:
        # makes sure its not a META value
        if not "META" in key:

            # checks if its already a value or another dict
            if not isinstance(data[key], dict):
                    data[key] = list_or_string(data[key])
            
            else:
                # values in dict
                for key2 in data[key]:
                    # another check if its a value or a dict (yes this code sucks)
                    if not isinstance(data[key][key2], dict):
                        data[key][key2] = list_or_string(data[key][key2])

                    else:
                        # values in dict in dict
                        for key3 in data[key][key2]:
                            # another check if its a value or a dict (yes this code sucks)
                            if not isinstance(data[key][key2][key3], dict):
                                data[key][key2][key3] = list_or_string(data[key][key2][key3])
                            
                            else:
                                # values in dict in dict in dict (OMFG)
                                for key4 in data[key][key2][key3]:
                                    data[key][key2][key3][key4] = list_or_string(data[key][key2][key3][key4])
                                
    write_json_data()



else:
    print(f"FILE {langJson} NOT FOUND!")