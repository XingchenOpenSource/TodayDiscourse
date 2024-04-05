from todaydiscourse import config
import os
import json
import random

current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)
directory = config.get_discourse_path()

def get_discourse():
    json_files = [file for file in os.listdir(directory) if file.endswith('.json')]
    discourse_file = random.choice(json_files)
    with open(os.path.join(directory, discourse_file), 'r', encoding='utf-8') as file:
        data = json.loads(file.read())
        selected_data = random.choice(data)

        final_data = {
            'status': '200',
            'msg': '成功',
            'category': os.path.splitext(discourse_file)[0],
            'content': selected_data.get('content'),
            'from': selected_data.get('from'),
            'creator': selected_data.get('creator'),
            'date': selected_data.get('date')
        }

    return final_data