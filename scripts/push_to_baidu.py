import xml.etree.ElementTree as ET
import requests

# 百度推送接口URL
api_url = "http://data.zz.baidu.com/urls?site=https://liangbm3.top&token=14kWwzpjAWdXa9B7"

# 本地XML文件路径
sitemap_path = "D:\\OneDrive - 中山大学\\桌面\\blogs\\public\\sitemap.xml"

# 解析XML文件
def parse_sitemap(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    urls = []
    
    # 假设XML格式为<sitemapindex>或<urlset>
    if root.tag.endswith('sitemapindex'):
        for sitemap in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}sitemap'):
            loc = sitemap.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text
            urls.append(loc)
    elif root.tag.endswith('urlset'):
        for url in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
            loc = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text
            urls.append(loc)
    
    return urls

# 推送单个URL到百度
def push_single_url_to_baidu(url):
    headers = {
        'Content-Type': 'text/plain'
    }
    
    response = requests.post(api_url, headers=headers, data=url)
    
    if response.status_code == 200:
        result = response.json()
        print(f"推送成功: {url}")
        print(f"成功推送的URL数量: {result.get('success', 0)}")
        print(f"当天剩余可推送的URL数量: {result.get('remain', 0)}")
        if 'not_same_site' in result:
            print(f"未处理的URL（不属于本站）: {result['not_same_site']}")
        if 'not_valid' in result:
            print(f"不合法的URL: {result['not_valid']}")
    else:
        print(f"推送失败: {url}, 状态码: {response.status_code}")
        print(response.text)

# 主函数
def main():
    urls = parse_sitemap(sitemap_path)
    if urls:
        for url in urls:
            push_single_url_to_baidu(url)
    else:
        print("未找到有效的URL。")

if __name__ == "__main__":
    main()