#!/usr/bin/env python3
"""
上传游戏页面到 Coze 对象存储
"""
import os
import sys
from pathlib import Path

# 添加 src 目录到 Python 路径
project_root = Path(__file__).parent.parent
src_path = project_root / "src"
sys.path.insert(0, str(src_path))

from storage.s3.s3_storage import S3SyncStorage


def upload_game_page():
    """上传游戏页面到对象存储"""
    print("开始上传游戏页面...")

    # 读取游戏文件
    game_file_path = project_root / "game.html"
    if not game_file_path.exists():
        print(f"错误：找不到游戏文件 {game_file_path}")
        return None

    with open(game_file_path, 'r', encoding='utf-8') as f:
        game_content = f.read()

    # 创建存储客户端（使用 workload identity，不需要手动提供 access_key 和 secret_key）
    try:
        # 注意：access_key 和 secret_key 是必需参数，但我们传入空字符串
        # 实际的认证会通过 x-storage-token header 完成
        storage = S3SyncStorage(
            access_key="",  # 留空，使用 workload identity
            secret_key="",  # 留空，使用 workload identity
            bucket_name=os.getenv("COZE_BUCKET_NAME", "coze-coding-project")
        )
    except Exception as e:
        print(f"创建存储客户端失败: {e}")
        return None

    # 上传文件
    try:
        object_key = storage.upload_file(
            file_content=game_content.encode('utf-8'),
            file_name="math_game.html",
            content_type="text/html"
        )
        print(f"✅ 上传成功！")
        print(f"对象键: {object_key}")

        # 生成访问链接
        endpoint_url = storage.endpoint_url or os.getenv("COZE_BUCKET_ENDPOINT_URL", "")
        if not endpoint_url:
            # 如果没有配置端点，返回对象键
            print(f"\n⚠️ 未配置对象存储端点，无法生成访问链接")
            print(f"对象键: {object_key}")
            return object_key

        # 构建访问 URL
        url = f"{endpoint_url}/{storage.bucket_name}/{object_key}"
        print(f"\n🎉 游戏页面已部署！")
        print(f"访问链接: {url}")

        return object_key

    except Exception as e:
        print(f"❌ 上传失败: {e}")
        import traceback
        traceback.print_exc()
        return None


def update_game_link(object_key):
    """更新游戏工具中的链接"""
    if not object_key:
        return

    tool_file = project_root / "src" / "tools" / "game_interaction_tool.py"

    if not tool_file.exists():
        print(f"警告：找不到工具文件 {tool_file}")
        return

    print(f"\n正在更新游戏链接...")
    with open(tool_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 生成新的 URL
    try:
        storage = S3SyncStorage(
            access_key="",  # 留空，使用 workload identity
            secret_key="",  # 留空，使用 workload identity
            bucket_name=os.getenv("COZE_BUCKET_NAME", "coze-coding-project")
        )
        endpoint_url = storage.endpoint_url or os.getenv("COZE_BUCKET_ENDPOINT_URL", "")
        url = f"{endpoint_url}/{storage.bucket_name}/{object_key}"
    except:
        url = object_key

    # 替换链接（替换 game_url 变量的值）
    old_url_pattern = r'game_url = "https://[^"]+?"'
    import re
    new_content = re.sub(
        old_url_pattern,
        f'game_url = "{url}"',
        content
    )

    if new_content != content:
        with open(tool_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✅ 游戏链接已更新: {url}")
    else:
        print(f"⚠️ 未找到需要更新的游戏链接")


if __name__ == "__main__":
    object_key = upload_game_page()
    if object_key:
        update_game_link(object_key)
        print("\n✅ 所有操作完成！")
    else:
        print("\n❌ 上传失败")
        sys.exit(1)
