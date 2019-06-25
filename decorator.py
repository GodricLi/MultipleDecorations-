# _*_ coding=utf-8 _*_


# 装饰器：执行index函数之前进行用户密码认证，之后再进行用户权限认证

def login(func):
    """
    外部函数，验证是否登录
    :param func: 执行函数的函数名
    :return: 内部函数名
    """
    print('login')
    def inner():
        """
        内部函数，认证逻辑
        :return: 外部函数的参数
        """
        # 假装这里是DB里面存的用户信息
        _username = 'alex'
        _password = '123'

        username = input('user:')
        password = input('password:')
        if username == _username and password == _password:
            # 返回需要执行函数名加上括号index()，执行index函数
            return func()
        else:
            print('Wrong Username Or Password!')

    return inner


def permission(func):
    """
    验证是否有权限
    :param func:
    :return:
    """
    print('permission')

    def inner_per():
        """
        验证权限逻辑
        :return:
        """
        print('permission allowed')

        return func()

    return inner_per

# 多个装饰器的调用顺序是自下往上，但是运行时的执行顺序是自上往下！！！
# 先验证有没有登录@login，再验证权限@permission，我们采用下面的顺序来装

@login          # index=login(index)——>index=inner,index()=login(index)()=inner()
@permission
def index():
    """
    需要执行的函数
    :return:
    """
    print('——————首页——————')


if __name__ == '__main__':
    index()
