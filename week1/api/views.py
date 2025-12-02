from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello(request, name="Eng.Nesma Ahmad"):
    data = {
        "message": "Hello, World!",
        "personalized": f"Hello, {name}"
    }
    return Response(data)
