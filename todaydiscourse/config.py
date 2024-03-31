import os
import json
from . import log

default_data = {
    'host': '0.0.0.0',
    'port': 8080
}

def get_config():
    json_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.json')
    if not os.path.exists(json_file_path):
        with open(json_file_path, 'w') as json_file:
            json.dump(default_data, json_file)
    else:
        with open(json_file_path, 'r') as json_file:
            try:
                data = json.load(json_file)
            except json.decoder.JSONDecodeError as e:
                log.error(f"JSON解析错误: {str(e)}")
                data = default_data
                
            if 'port' not in data:
                log.warning("配置文件中缺少'port'字段，使用默认值。")
                data['port'] = default_data['port']

            if 'host' not in data:
                log.warning("配置文件中缺少'host'字段，使用默认值。")
                data['host'] = default_data['host']

json_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.json')
def get_config_port():
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        return data.get('port', 0)

def get_config_host():
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        return data.get('host', 0)