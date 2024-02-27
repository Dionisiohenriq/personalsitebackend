from django.http import JsonResponse

def index(request):
    return JsonResponse({'message': 'Hello from Django!'})

def get_data(request):
    data = {'message': 'Dados do backend'}
    return JsonResponse(data)