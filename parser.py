import json

with open("pretty_outfile.json", "r") as f:
    json_object = json.load(f)
print(len(json_object['data']))

def main():
    
