# coding=utf-8

# q67g039lo.bkt.clouddn.com
from qiniu import Auth, put_data, etag
import qiniu.config
#需要填写你的 Access Key 和 Secret Key
access_key = '1wBjfGouNgh13uj8bymN8XZBj-6X-yuejR_s7V9x'
secret_key = 'Bg6nNGMu-ovQvKXMatHhbtkwhwB-Gawlwq6Y8pav'

def storage(image_data):
    # 构建鉴权对象
    if not image_data:
        return None
    q = Auth(access_key, secret_key)
    # 要上传的空间
    bucket_name = 'ihomefan'
    # 上传后保存的文件名
    # key = 'my-python-logo.png'
    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, None, 3600)
    # 要上传文件的本地路径
    # localfile = './sync/bbb.jpg'
    ret, info = put_data(token, None, image_data)
    print(info)
    return ret['key']

if __name__ == '__main__':
    fileName = input('请输入文件名：')
    with open(fileName, 'rb') as f:
        fileData = f.read()
    key = storage(fileData)
    print(key)
