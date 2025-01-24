import requests

# 定义要提交的URL列表
urls = [
    'http://www.example.com/1.html',
    'http://www.example.com/2.html'
]

# 定义API端点和token
api = 'http://data.zz.baidu.com/urls?site=https://liangbm3.top&token=14kWwzpjAWdXa9B7'

# 准备请求数据
data = "\n".join(urls)
headers = {
    'Content-Type': 'text/plain'
}

# 发送POST请求
response = requests.post(api, data=data, headers=headers)

# 输出结果
print(response.text)