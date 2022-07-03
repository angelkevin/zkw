# from django.http import HttpResponse
# from django.shortcuts import render
# from pyecharts.charts import Geo, Bar, Pie
# from pyecharts.faker import Faker
# from werkzeug.routing import Map
# from pyecharts import options as opts
#
# import pymysql
#
# db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='mydatabase')
#
#
# def load(request):
#     return render(request, '1.html')
#
#
# def login(request):
#     username = request.GET.get('username')
#     password = request.GET.get('password')
#
#     sql = f"SELECT passworld FROM user WHERE account={username};"
#
#     mycursor = db.cursor()
#     mycursor.execute(sql)
#     pwd = mycursor.fetchall()
#     db.commit()
#
#     if pwd[0][0] == password:
#         return render(request, '2.html')
#     return HttpResponse(u'登录失败')
#
#
# def signup(request):
#     return render(request, "signup.html")
#
#
# def singup_1(request):
#     username = request.GET.get('username')
#     password = request.GET.get('password')
#     sql = f"INSERT INTO user values('{username}','{password}');"
#     mycursor = db.cursor()
#     mycursor.execute(sql)
#     db.commit()
#     return render(request, "1.html")
