#!/usr/bin/env python3
"""
简单的Helloworld Web应用
使用Python内置的HTTP服务器实现
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class HelloWorldHandler(BaseHTTPRequestHandler):
    """处理HTTP请求的处理器"""
    
    def do_GET(self):
        """处理GET请求"""
        # 设置响应头
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        # 根据路径返回不同的内容
        if self.path == '/':
            content = self.get_index_page()
        elif self.path == '/hello':
            content = self.get_hello_world()
        elif self.path.startswith('/hello/'):
            name = self.path.split('/')[-1]
            content = self.get_hello_name(name)
        else:
            content = self.get_404_page()
        
        # 发送响应内容
        self.wfile.write(content.encode('utf-8'))
    
    def get_index_page(self):
        """首页内容"""
        return """
        <!DOCTYPE html>
        <html lang="zh-CN">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Helloworld应用</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: #f5f5f5;
                }
                .container {
                    background: white;
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                }
                h1 {
                    color: #333;
                    border-bottom: 2px solid #007bff;
                    padding-bottom: 10px;
                }
                .feature-list {
                    list-style-type: none;
                    padding: 0;
                }
                .feature-list li {
                    background: #e7f3ff;
                    margin: 10px 0;
                    padding: 10px 15px;
                    border-radius: 5px;
                    border-left: 4px solid #007bff;
                }
                .links {
                    margin-top: 30px;
                }
                .links a {
                    display: inline-block;
                    margin-right: 15px;
                    padding: 10px 20px;
                    background: #007bff;
                    color: white;
                    text-decoration: none;
                    border-radius: 5px;
                    transition: background 0.3s;
                }
                .links a:hover {
                    background: #0056b3;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Helloworld Web应用</h1>
                <p style="font-size: 18px; color: #666;">欢迎使用简单的Python Web应用！</p>
                
                <h2>功能特性：</h2>
                <ul class="feature-list">
                    <li>基于Python内置HTTP服务器</li>
                    <li>无需额外依赖</li>
                    <li>支持动态路由</li>
                    <li>响应式设计</li>
                </ul>
                
                <div class="links">
                    <a href="/hello">基础Hello World</a>
                    <a href="/hello/Django">个性化问候</a>
                </div>
            </div>
        </body>
        </html>
        """
    
    def get_hello_world(self):
        """Hello World页面"""
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Hello World</title>
            <style>
                body { font-family: Arial; text-align: center; padding: 50px; }
                h1 { color: #007bff; }
                a { color: #007bff; text-decoration: none; }
            </style>
        </head>
        <body>
            <h1>Hello, World!</h1>
            <p>欢迎来到Helloworld应用！</p>
            <p><a href="/">返回首页</a></p>
        </body>
        </html>
        """
    
    def get_hello_name(self, name):
        """个性化问候页面"""
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Hello {name}</title>
            <style>
                body {{ font-family: Arial; text-align: center; padding: 50px; }}
                h1 {{ color: #28a745; }}
                a {{ color: #007bff; text-decoration: none; }}
            </style>
        </head>
        <body>
            <h1>Hello, {name}!</h1>
            <p>很高兴见到你！</p>
            <p><a href="/">返回首页</a></p>
        </body>
        </html>
        """
    
    def get_404_page(self):
        """404页面"""
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>页面未找到</title>
            <style>
                body { font-family: Arial; text-align: center; padding: 50px; }
                h1 { color: #dc3545; }
                a { color: #007bff; text-decoration: none; }
            </style>
        </head>
        <body>
            <h1>404 - 页面未找到</h1>
            <p>抱歉，您访问的页面不存在。</p>
            <p><a href="/">返回首页</a></p>
        </body>
        </html>
        """

def run_server(port=8000):
    """运行HTTP服务器"""
    server_address = ('', port)
    httpd = HTTPServer(server_address, HelloWorldHandler)
    
    print(f"服务器运行在 http://localhost:{port}")
    print("可用路由:")
    print("  - /          首页")
    print("  - /hello     基础Hello World")
    print("  - /hello/名字 个性化问候")
    print("按 Ctrl+C 停止服务器")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器已停止")

if __name__ == '__main__':
    run_server()