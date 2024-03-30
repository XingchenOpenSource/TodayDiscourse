import os
import json
from urllib.parse import urlparse, parse_qs
import random

current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)
directory = os.path.join(current_directory,"TodayDiscourse")

def handle_td_request(handler,query_params):
    json_files = [file for file in os.listdir(directory) if file.endswith('.json')]
    random_json_file = random.choice(json_files)
    site_param_main = query_params.get('type')
    handler.send_response(200)
    with open(os.path.join(directory, random_json_file), 'r', encoding='utf-8') as file:
        data = json.loads(file.read())
        selected_data = random.choice(data)
        # 复制先前的数据到新字典中
        final_data = {
            'status': '200',
            'msg': '成功',
            'content': selected_data.get('content'),
            'from': selected_data.get('from'),
            'creator': selected_data.get('creator'),
            'date': selected_data.get('date')
            }
    handler.send_header('Content-type', 'application/json')
    handler.end_headers()
    handler.wfile.write(json.dumps(final_data, ensure_ascii=False).encode())
    file.close()