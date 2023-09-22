import json

# Saves airplane dictionary in txt file
def save_airplane(airplane, file_name):
    with open(file_name, 'w') as file:
        file.write(json.dumps(airplane))

def load_airplane(file_name):
    # Opening JSON file
    airplane = {}
    with open(file_name) as json_file:
        airplane = json.load(json_file)
    return airplane