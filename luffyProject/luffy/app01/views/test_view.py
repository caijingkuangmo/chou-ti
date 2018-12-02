from django.shortcuts import HttpResponse
from django_redis import get_redis_connection

def test(request, *args, **kwargs):
    conn = get_redis_connection()
    conn.set('age', 18)
    print(conn.get('age'))
    return HttpResponse('ok')