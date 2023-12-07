

import json
def get_title_for_json_file(user_text):
    with open("source/pars.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    titles = []
    for item in data:
        if (item["title"]).find(user_text) !=-1:
            titles.append(item)
        else:
            continue

    return titles

#get_title_for_json_file("П")