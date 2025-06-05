import os
import json
from datetime import datetime

def generate_articles_json():
    articles = []
    base_dir = 'article'

    for category in os.listdir(base_dir):
        category_path = os.path.join(base_dir, category)
        if os.path.isdir(category_path):
            for file in os.listdir(category_path):
                if file.endswith('.md'):
                    file_path = os.path.join(category_path, file)
                    mtime = os.path.getmtime(file_path)

                    # 读取前200个字符作为摘要
                    with open(file_path, 'r', encoding='utf-8') as f:
                        excerpt = f.read(200).strip() + '...'

                    articles.append({
                        "title": file.replace('.md', ''),
                        "category": category,
                        "path": file_path.replace('\\', '/'),
                        "lastModified": datetime.fromtimestamp(mtime).isoformat(),
                        "excerpt": excerpt
                    })

    # 按修改时间排序
    articles.sort(key=lambda x: x['lastModified'], reverse=True)

    # 保存到文件
    with open('data/article.json', 'w', encoding='utf-8') as f:
        json.dump(articles, f, indent=2, ensure_ascii=False)

    print(f"生成 {len(articles)} 篇文章索引")

if __name__ == "__main__":
    generate_articles_json()