#!/usr/bin/env python3
"""
上传游戏页面到 TOS bucket
"""
import os
import sys
from pathlib import Path

# 添加 src 目录到 Python 路径
project_root = Path(__file__).parent.parent
src_path = project_root / "src"
sys.path.insert(0, str(src_path))

from storage.s3.s3_storage import S3SyncStorage


def upload_to_tos():
    """上传游戏页面到 TOS bucket"""
    print("开始上传游戏页面到 TOS...")

    # 读取游戏文件
    game_file_path = project_root / "game.html"
    if not game_file_path.exists():
        print(f"错误：找不到游戏文件 {game_file_path}")
        return None

    with open(game_file_path, 'r', encoding='utf-8') as f:
        game_content = f.read()

    # 创建存储客户端，使用已知的 TOS bucket
    # 从之前的链接中提取：coze_storage_7599855582224318498
    tos_bucket = "coze_storage_7599855582224318498"

    print(f"TOS Bucket: {tos_bucket}")

    try:
        storage = S3SyncStorage(
            access_key="",
            secret_key="",
            bucket_name=tos_bucket
        )
    except Exception as e:
        print(f"创建存储客户端失败: {e}")
        return None

    # 上传文件
    try:
        object_key = storage.upload_file(
            file_content=game_content.encode('utf-8'),
            file_name="math_game.html",
            content_type="text/html",
            bucket=tos_bucket
        )
        print(f"✅ 上传成功！")
        print(f"对象键: {object_key}")
        print(f"Bucket: {tos_bucket}")

        # TOS 签名 URL 模式
        # https://coze-coding-project.tos.coze.site/coze_storage_7599855582224318498/math_game_*.html?sign=...
        # 注意：这里需要实际的签名生成逻辑
        # 我们返回对象键和 bucket 名称，用户需要手动构建签名 URL

        print(f"\n📝 文件信息：")
        print(f"   Bucket: {tos_bucket}")
        print(f"   Object Key: {object_key}")
        print(f"\n⚠️ 注意：需要使用 TOS SDK 生成签名 URL 才能公网访问")
        print(f"   签名 URL 格式：")
        print(f"   https://coze-coding-project.tos.coze.site/{tos_bucket}/{object_key}?sign=...")

        return {
            "bucket": tos_bucket,
            "object_key": object_key
        }

    except Exception as e:
        print(f"❌ 上传失败: {e}")
        import traceback
        traceback.print_exc()
        return None


if __name__ == "__main__":
    result = upload_to_tos()
    if result:
        print("\n✅ 上传完成！")
        print("\n💡 下一步：需要生成签名 URL")
        print("   请联系管理员或使用 TOS SDK 生成带签名的访问链接")
    else:
        print("\n❌ 上传失败")
        sys.exit(1)
