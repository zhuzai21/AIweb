import requests
import os

# 确保图片目录存在
image_dir = '/Users/zhujianbin/Desktop/AI代码/AIweb/public/images'
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

# 定义要下载的图片URL
urls = [
    'https://images.unsplash.com/photo-1677442136019-21780ecad995?ixlib=rb-4.0.3',  # AI technology
    'https://images.unsplash.com/photo-1682687220742-aba13b6e50ba?ixlib=rb-4.0.3',  # Machine learning
    'https://images.unsplash.com/photo-1485827404703-89b55fcc595e?ixlib=rb-4.0.3'   # Digital technology
]

# 下载图片
for i, url in enumerate(urls, 1):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            file_path = os.path.join(image_dir, f'banner{i}.jpg')
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f'Successfully downloaded banner{i}.jpg')
        else:
            print(f'Failed to download banner{i}.jpg: HTTP {response.status_code}')
    except Exception as e:
        print(f'Error downloading banner{i}.jpg: {e}')
