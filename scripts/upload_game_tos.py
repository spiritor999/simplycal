#!/usr/bin/env python3
"""
上传游戏页面到 Coze 对象存储（TOS 端点）
"""
import os
import sys
import hashlib
import hmac
import time
from urllib.parse import urlencode
from pathlib import Path

# 添加 src 目录到 Python 路径
project_root = Path(__file__).parent.parent
src_path = project_root / "src"
sys.path.insert(0, str(src_path))

from storage.s3.s3_storage import S3SyncStorage


def generate_tos_signed_url(bucket_name: str, object_key: str, endpoint_url: str) -> str:
    """
    生成 TOS 签名 URL

    注意：这里需要根据实际的 TOS 签名算法实现
    简化版本：使用 endpoint_url + bucket + object_key
    """
    # 如果 endpoint_url 已经是 TOS 端点，直接构建 URL
    if 'tos.coze.site' in endpoint_url:
        # TOS 端点格式：https://coze-coding-project.tos.coze.site
        # URL 格式：https://coze-coding-project.tos.coze.site/bucket/object_key
        return f"{endpoint_url}/{bucket_name}/{object_key}"
    else:
        # 集成端点，需要签名
        # 这里简化处理，直接返回 URL
        return f"{endpoint_url}/{bucket_name}/{object_key}"


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

    # 创建存储客户端
    try:
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

        # 获取端点 URL
        endpoint_url = storage.endpoint_url or os.getenv("COZE_BUCKET_ENDPOINT_URL", "")
        bucket_name = storage.bucket_name

        print(f"\n端点 URL: {endpoint_url}")
        print(f"桶名: {bucket_name}")

        # 判断端点类型并生成 URL
        if 'tos.coze.site' in endpoint_url:
            # TOS 端点，生成签名 URL
            # 注意：实际签名需要使用 TOS SDK 或签名算法
            # 这里简化为直接构建 URL（需要桶名配置正确）
            url = f"https://coze-coding-project.tos.coze.site/coze_storage_7599855582224318498/{object_key}"
            print(f"\n🎉 游戏页面已部署！")
            print(f"访问链接: {url}")
            print(f"\n⚠️ 注意：此链接可能需要配置签名才能访问")
            print(f"如需公网访问，请使用 TOS SDK 生成带签名的 URL")
        else:
            # 集成端点，需要 token 认证
            url = f"{endpoint_url}/{bucket_name}/{object_key}"
            print(f"\n⚠️ 此链接需要通过 Coze 平台认证访问")
            print(f"建议使用本地服务器访问游戏")

        return object_key

    except Exception as e:
        print(f"❌ 上传失败: {e}")
        import traceback
        traceback.print_exc()
        return None


if __name__ == "__main__":
    object_key = upload_game_page()
    if object_key:
        print("\n✅ 上传完成！")
        print("\n💡 推荐访问方式：")
        print("   1. 本地服务器：python scripts/start_game_server.py")
        print("   2. 本地文件：直接打开 game.html")
    else:
        print("\n❌ 上传失败")
        sys.exit(1)
