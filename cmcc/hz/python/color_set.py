# 定义了一个函数
def colored(color, text):
    # Python3 字典
    table = {
        'red': '\033[91m',
        'green': '\033[92m',
        # no color
        'nc': '\033[0m'
    }
    # 字典取值的方法
    cv = table.get(color)
    # 字典取值的方法
    nc = table.get('nc')
    # 返回一个颜色的表达式
    return ''.join([cv, text, nc])