#!/usr/bin/env python3
"""
上传文件并生成 TOS 签名 URL（支持自定义文件名）
"""
import os
import sys
from pathlib import Path

# 添加工作目录到 Python 路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from coze_coding_dev_sdk.s3 import S3SyncStorage


def upload_file_with_signed_url(file_path: str, object_name: str) -> str:
    """
    上传文件并生成签名 URL

    Args:
        file_path: 本地文件路径（相对于项目根目录）
        object_name: 存储对象名称（如 "agent.html" 或 "math_game.html"）

    Returns:
        签名 URL
    """
    print(f"开始上传文件: {file_path} -> {object_name}...")

    # 读取文件
    full_path = project_root / file_path
    if not full_path.exists():
        print(f"错误：找不到文件 {full_path}")
        return None

    with open(full_path, 'r', encoding='utf-8') as f:
        file_content = f.read()

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
            file_content=file_content.encode('utf-8'),
            file_name=object_name,
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
    # 支持命令行参数
    if len(sys.argv) >= 3:
        file_path = sys.argv[1]
        object_name = sys.argv[2]
    else:
        print("用法: python upload_any_file.py <本地文件路径> <存储对象名称>")
        print("\n示例:")
        print("  python upload_any_file.py assets/agent.html agent.html")
        print("  python upload_any_file.py assets/math_game.html math_game.html")
        sys.exit(1)

    signed_url = upload_file_with_signed_url(file_path, object_name)
    if signed_url:
        print("\n" + "="*60)
        print("✅ 所有操作完成！")
        print("="*60)
        print("\n💡 使用建议：")
        print(f"   1. 点击上面的链接测试文件是否可访问")
        print(f"   2. 对象名称: {object_name}")
        print("   3. 链接有效期：1年")
    else:
        print("\n❌ 操作失败")
        sys.exit(1)
