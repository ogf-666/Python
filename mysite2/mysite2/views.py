from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):

    # # return HttpResponse('This is index')
    #
    # # 1 通过loader加载模板
    # t = loader.get_template('test.html')
    #
    # # 2 t对象转化成html字符串
    # html = t.render()
    #
    # # 3 将html return 到 浏览器
    # return HttpResponse(html)

    # render 方案
    dic = {'username':'guodegang','age':42}
    return render(request,'test.html',dic)

def test_p(request):
    # 测试页面传参
    dic = {}
    dic['lst'] = ['张三','李四','王五']
    dic['dict'] = {'username':'guodegang'}
    dic['class_obj'] = Dog()
    dic['say_hi'] = say_hi
    dic['script'] = '<script>alert(111)</script>'
    dic['number'] = 1
    return render(request, 'test_p.html', dic)


class Dog:
    def say(self):
        return 'say say say say'

def say_hi():
    return 'say hi'

def test_if(request):
    dic = {
        "a": "4",
        "b": "3.5",
    }
    return render(request, 'test_if.html',dic)

def test_js(request):

    if request.method == 'GET':
        return render(request, 'test_js.html')

    elif request.method == 'POST':

        x = int(request.POST.get('x'))
        op = request.POST.get('op')
        y = int(request.POST.get('y'))

        print(66666)
        print(x)
        print(op)
        print(y)
        print(99999)




        return HttpResponse('-----jaenenrfjsv-----')



def shebao_view(request):
    if request.method == 'GET':
        # 显示静态页面
        return render(request, 'shebao.html')
    elif request.method == 'POST':
        # 处理数据
        base = int(request.POST.get('base'))
        # 检查base 是否在 这个区间 3082~23118
        if base > 23118:
            base = 23118
        if base < 3082:
            base = 3082
        is_city = int(request.POST.get('is_city'))

        # 养老金
        z_old = base * 0.08  # 个人缴纳
        d_old = base * 0.19  # 单位缴纳

        # 工伤
        z_compo = base * 0
        d_compo = base * 0.005

        # 医疗
        z_medical = base * 0.02 + 3
        d_medical = base * 0.1

        # 生育
        z_bearing = base * 0
        d_bearing = base * 0.008

        # 公积金
        z_fund = base * 0.12
        d_fund = base * 0.12


        if is_city:
            # 城市户口
            # 失业
            z_idleness = base * 0.002
            d_idleness = base * 0.008

            z_restur = z_old + z_idleness + z_compo + z_medical + z_bearing + z_fund
            d_restur = d_old + d_idleness + d_compo + d_medical + d_bearing + d_fund
            gj_restur = z_restur + d_restur
        else:
            # 农村户口
            # 失业
            z_idleness = base * 0
            d_idleness = base * 0.008

            z_restur = z_old + z_idleness + z_compo + z_medical + z_bearing + z_fund
            d_restur = d_old + d_idleness + d_compo + d_medical + d_bearing + d_fund
            gj_restur = z_restur + d_restur

        return render(request, 'shebao.html', locals())













