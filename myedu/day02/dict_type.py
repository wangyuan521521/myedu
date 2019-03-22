
import json
# 声明一个全量 dict 变量 （字典）
adict = {"name":"wy","pwd":"123456"}

# 这是一个字符串 不过他是json 格式，也是字典的格式
adictstr = '{"name":"wy","pwd":"123456","1":"数字"}'

if __name__ == '__main__':
    # print(adict)
    # adict.pop('name')
    # print(adict['name'])
    # print(adict)
    # print(type(adictstr))
    # dict_str = json.loads(adictstr)
    # print(type(dict_str))
    # print(dict_str['name'])
    loads = json.loads(adictstr)
    print(type(loads))

    dumps = json.dumps(adict)
    print(type(dumps))

    dumps = json.dumps(loads,ensure_ascii=False)
    print(dumps)

