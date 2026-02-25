#!/usr/bin/env python3
"""
启动本地游戏服务器
"""
import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

# 设置项目根目录
project_root = Path(__file__).parent.parent
os.chdir(project_root)

class GameHTTPRequestHandler(SimpleHTTPRequestHandler):
    """自定义 HTTP 请求处理器"""

    def end_headers(self):
        """设置 CORS 头"""
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_GET(self):
        """处理 GET 请求"""
        # 如果请求的是游戏页面，返回 game.html
        if self.path == '/' or self.path == '/game.html':
            self.path = '/game.html'
        return super().do_GET()


def start_server(port=8080):
    """启动服务器"""
    try:
        server_address = ('', port)
        httpd = HTTPServer(server_address, GameHTTPRequestHandler)
        print(f"✅ 游戏服务器已启动！")
        print(f"🎮 游戏链接: http://localhost:{port}/game.html")
        print(f"📁 工作目录: {project_root}")
        print(f"\n按 Ctrl+C 停止服务器\n")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n🛑 服务器已停止")
        sys.exit(0)
    except OSError as e:
        print(f"❌ 端口 {port} 已被占用，请尝试其他端口")
        print(f"💡 提示：使用不同的端口启动：python scripts/start_game_server.py <端口号>")
        sys.exit(1)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='启动游戏服务器')
    parser.add_argument('--port', type=int, default=8080, help='端口号（默认：8080）')
    args = parser.parse_args()

    start_server(args.port)
