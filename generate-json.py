import os
import json
from datetime import datetime

def generate_articles_json(lang='zh'):
    articles = []
    base_dir = f'article/{lang}'  # 支持 zh/en 子目录

    for category in os.listdir(base_dir):
        category_path = os.path.join(base_dir, category)
        if os.path.isdir(category_path):
            for file in os.listdir(category_path):
                if file.endswith('.md'):
                    file_path = os.path.join(category_path, file)
                    mtime = os.path.getmtime(file_path)

                    with open(file_path, 'r', encoding='utf-8') as f:
                        first_line = f.readline().strip()
                        if first_line.startswith('# '):
                            title = first_line[2:].strip()
                        else:
                            title = file.replace('.md', '').replace('_en', '')
                        # 回到文件开头读取摘要（如果需要）
                        f.seek(0)
                        excerpt = f.read(200).strip() + '...'

                    articles.append({
                        "title": title,
                        "category": category,
                        "path": file_path.replace('\\', '/'),
                        "lastModified": datetime.fromtimestamp(mtime).isoformat(),
                        "excerpt": excerpt,
                        "lang": lang
                    })

    articles.sort(key=lambda x: x['lastModified'], reverse=True)

    os.makedirs(f'data/{lang}', exist_ok=True)
    with open(f'data/{lang}/article.json', 'w', encoding='utf-8') as f:
        json.dump(articles, f, indent=2, ensure_ascii=False)

    print(f"{lang} 生成 {len(articles)} 篇文章索引")

if __name__ == "__main__":
    generate_articles_json('zh')
    generate_articles_json('en')
