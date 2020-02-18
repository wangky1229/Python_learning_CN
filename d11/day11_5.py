import requests
import json


def main():
    resp = requests.get('http://api.tianapi.com/sicprobe/index?key=07e687edfdec520fbefabf0f97459154&num=20')
    data_model = json.loads(resp.text)
    for news in data_model['newslist']:
        print(news['title'])
        print(news['url'])
    try:
        with open('test.json', 'w', encoding='utf-8') as fs:
            json.dump(data_model['newslist'], fs)
    except IOError as e:
        print(e)
    print('保存数据完成!')

if __name__ == '__main__':
    main()