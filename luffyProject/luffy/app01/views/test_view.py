from django.shortcuts import HttpResponse
from django_redis import get_redis_connection
from django.core.cache import cache

def test(request, *args, **kwargs):
    # conn = get_redis_connection()
    # conn.set('age', 18)
    # print(conn.get('age'))
    cache.set('k100', 100)  #这里的cache指的是哪
    print(cache.get('k100'))
    return HttpResponse('ok')