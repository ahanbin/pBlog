// 步骤1：获取所有文章文件路径
async function fetchArticleList() {
    const response = await fetch('/list-articles'); // 需后端API支持（见下文）
    return response.json();
}

// 步骤2：按修改时间排序并渲染列表
function renderArticles(articles) {
    const sortedArticles = articles.sort((a, b) =>
        new Date(b.lastModified) - new Date(a.lastModified)
    );

    const listContainer = document.getElementById('article-list');
    sortedArticles.forEach(article => {
        const articleEl = document.createElement('article');
        articleEl.innerHTML = `
      <h2><a href="${article.path}">${article.title}</a></h2>
      <p>分类：${article.category} | 更新时间：${article.lastModified}</p>
    `;
        listContainer.appendChild(articleEl);
    });
}

// 步骤3：生成分类导航
function renderCategories(articles) {
    const categories = [...new Set(articles.map(article => article.category))];
    const navContainer = document.getElementById('category-list');

    categories.forEach(category => {
        const li = document.createElement('li');
        li.textContent = category;
        li.addEventListener('click', () => filterByCategory(category));
        navContainer.appendChild(li);
    });
}

// 初始化
(async () => {
    const articles = await fetchArticleList();
    renderArticles(articles);
    renderCategories(articles);
})();