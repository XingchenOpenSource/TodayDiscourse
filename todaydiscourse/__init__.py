import http.server
import socketserver
import os
import log
import json
import sys
from urllib.parse import urlparse, parse_qs
import core
current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)
# JSON文件路径
json_file_path = os.path.join(current_directory, 'settings.json')

default_data = {
    'port': 8080
}

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
        update_data = {'port': 8080}
        data.update(update_data)

    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file)

port = 0
with open(json_file_path, 'r') as json_file:
    file_content = json_file.read()
    if file_content:
        data = json.loads(file_content)
        port = data.get('port', 0)

log.info("欢迎使用 TodayDiscourse 今日话语")
log.info("开发团队: XingchenOpenSource 星辰开源")
log.info("团队地址: https://github.com/XingchenOpenSource")
log.info("项目地址: https://github.com/XingchenOpenSource/TodayDiscourse")
log.info(f"今日话语已启动  浏览器打开 http://localhost:{port} 访问")
        
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        log.info("请求IP: {} 请求内容: {}".format(self.client_address[0], format%args))
    def do_GET(self):
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
        if self.path == '/':
            core.handle_td_request(self,query_params)
        else:
            response_data = {
                'status': '404',
                'msg': '失败'
            }   
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response_data, ensure_ascii=False).encode())

with socketserver.TCPServer(("", port), MyHandler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        log.info("今日话语正在退出...感谢您的使用")
        httpd.server_close()
        sys.exit(0)
