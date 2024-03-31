from flask import Flask, request, jsonify
import os
import json
from . import log, core

# 获取当前文件路径和目录
current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)
json_file_path = os.path.join(current_directory, 'settings.json')

default_data = {
    'port': 8080
}

def configure_json_file():
    # 初始化或修复 settings.json 文件
    if not os.path.exists(json_file_path):
        with open(json_file_path, 'w') as json_file:
            json.dump(default_data, json_file)
    else:
        with open(json_file_path, 'r') as json_file:
            try:
                data = json.load(json_file)
            except json.decoder.JSONDecodeError:
                data = default_data
                
            if 'port' not in data:
                data['port'] = default_data['port']

        with open(json_file_path, 'w') as json_file:
            json.dump(data, json_file)

def read_port_from_json():
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        return data.get('port', 0)

def handle_td_request(query_params):
    return core.handle_td_request(request, query_params)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    log.warning("请求IP: {} 请求内容: 错误！调用方式错误！".format(request.remote_addr))
    return "欢迎今日话语！您的调用方式错误。", 500

@app.route('/text', methods=['GET'])
def text_endpoint():
    text = handle_td_request(request.args).get('content', 0)
    return text, 200, {'Content-Type': 'text/plain'}

@app.route('/json', methods=['GET'])
def json_endpoint():
    response_data = handle_td_request(request.args)
    return jsonify(response_data), 200

def start_flask_server():
    configure_json_file()
    server_port = read_port_from_json()

    app.run(host='0.0.0.0', port=server_port, threaded=True)

    log.info(f"🎉恭喜您！今日话语已在 http://localhost:{server_port} 上启动，请参阅官方文档以查看如何调用。")

if __name__ == '__main__':
    log.info("欢迎使用 TodayDiscourse 今日话语")
    log.info("开发团队: XingchenOpenSource 星辰开源")
    log.info("项目地址: https://github.com/XingchenOpenSource/TodayDiscourse")
    log.info("官方文档: https://xingchenopensource.github.io/apis/todaydiscourse/")
    start_flask_server()