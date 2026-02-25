#!/usr/bin/env python3
"""
上传游戏页面并生成 TOS 签名 URL
"""
import os
import sys
from pathlib import Path

# 添加工作目录到 Python 路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from coze_coding_dev_sdk.s3 import S3SyncStorage


def upload_game_with_signed_url():
    """上传游戏页面并生成签名 URL"""
    print("开始上传游戏页面...")

    # 读取游戏文件
    game_file_path = project_root / "game.html"
    if not game_file_path.exists():
        print(f"错误：找不到游戏文件 {game_file_path}")
        return None

    with open(game_file_path, 'r', encoding='utf-8') as f:
        game_content = f.read()

    # 初始化存储客户端
    try:
        storage = S3SyncStorage(
            endpoint_url=os.getenv("COZE_BUCKET_ENDPOINT_URL"),
            access_key="",
            secret_key="",
            bucket_name=os.getenv("COZE_BUCKET_NAME"),
            region="cn-beijing",
        )
        print(f"✅ 存储客户端初始化成功")
        print(f"   Bucket: {os.getenv('COZE_BUCKET_NAME')}")
        print(f"   Endpoint: {os.getenv('COZE_BUCKET_ENDPOINT_URL')}")
    except Exception as e:
        print(f"❌ 创建存储客户端失败: {e}")
        return None

    # 上传文件
    try:
        object_key = storage.upload_file(
            file_content=game_content.encode('utf-8'),
            file_name="math_game.html",
            content_type="text/html",
        )
        print(f"✅ 上传成功！")
        print(f"   对象键: {object_key}")
    except Exception as e:
        print(f"❌ 上传失败: {e}")
        import traceback
        traceback.print_exc()
        return None

    # 生成签名 URL
    try:
        # 签名 URL 有效期 1 年（31536000 秒）
        signed_url = storage.generate_presigned_url(
            key=object_key,
            expire_time=31536000  # 1年
        )
        print(f"\n🎉 签名 URL 生成成功！")
        print(f"\n访问链接:")
        print(f"{signed_url}")

        # 检查是否是 TOS 端点
        if 'tos.coze.site' in signed_url:
            print(f"\n✅ 这是 TOS 签名链接，可以直接公网访问！")
        else:
            print(f"\n⚠️ 注意：这可能不是 TOS 端点，请确认链接可访问")

        return signed_url

    except Exception as e:
        print(f"❌ 生成签名 URL 失败: {e}")
        import traceback
        traceback.print_exc()
        return None


if __name__ == "__main__":
    signed_url = upload_game_with_signed_url()
    if signed_url:
        print("\n" + "="*60)
        print("✅ 所有操作完成！")
        print("="*60)
        print("\n💡 使用建议：")
        print("   1. 点击上面的链接测试游戏是否可访问")
        print("   2. 如需更新智能体链接，复制此链接到 game_interaction_tool.py")
        print("   3. 链接有效期：1年")
    else:
        print("\n❌ 操作失败")
        sys.exit(1)
