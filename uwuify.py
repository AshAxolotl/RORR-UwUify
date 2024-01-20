import json
import os.path
import re

# The json file taken as input
input_json = "lang_from_bui.json"

# The json file created as output (I recommend to NOT make this the same as the input to not replace the file)
output_json = "uwu-engwish/lang.json"


# Replaces text using regex (Change this function if you want it to do something else then uwuify)
def text_replace(text: str):
    # replaces all L and R to W
    text = re.sub("[rl]+(?![^<]*\>)", "w", text)
    text = re.sub("[RL]+(?![^<]*\>)", "W", text)

    # replaces: the to de, they to dey, is to ish
    text = re.sub(r"\b(the)\b", "de", text)
    text = re.sub(r"\b(they)\b", "dey", text)
    text = re.sub(r"\b(is)\b", "ish", text)

    # same as above but when starting with a capital letter
    text = re.sub(r"\b(The)\b", "De", text)
    text = re.sub(r"\b(They)\b", "Dey", text)
    text = re.sub(r"\b(Is)\b", "Ish", text)

    # same as above but when all caps
    text = re.sub(r"\b(THE)\b", "DE", text)
    text = re.sub(r"\b(THEY)\b", "DEY", text)
    text = re.sub(r"\b(IS)\b", "ISH", text)

    return text



# Reads the input json file and returns in contents 
def read_json_data():
    with open(input_json, "r") as file:
        fileContents = file.read()

    data = json.loads(fileContents)

    return data

# Writes the output json file 
def write_json_data(data: dict):
    formatted_json = json.dumps(data, indent=4)
    with open(output_json, "w") as file:
        file.write(formatted_json)

# Handles the diffrent types of data
def replace(value):
    if isinstance(value, str):
        value = text_replace(value)

    elif isinstance(value, list):
        for i in range(len(value)):
            value[i] = replace(value[i])

    elif isinstance(value, dict):
        for key in value:
            value[key] = replace(value[key])
    
    return value


if os.path.isfile(input_json):
    json_data = read_json_data()
    json_data = replace(json_data)
    write_json_data(json_data)
    print(f"{output_json} has been made")

else:
    print(f"ERROR: {input_json} was not found! (try changing the input_json)")