from django.http import JsonResponse

# Create your views here.

from App.models import User
def list_user(request):
    # 业务罗
    data = User.objects.all()
    print(data)
    data = list(data)

    # 转换为列表套字典
    result = []
    for user in data:
        result.append({'uid':user.uid,'username':user.username})
    print(result)

    return JsonResponse(result,safe=False)

