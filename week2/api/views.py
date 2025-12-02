from rest_framework.decorators import api_view
from rest_framework.response import Response

# / → index()
@api_view(['GET'])
def index(request):
    data = {
        "title": "Welcome to the Index Page",
        "welcome_message": "This is an example of a home page displaying JSON data from Django REST Framework."
    }
    return Response(data)

# /about → about()
@api_view(['GET'])
def about(request):
    data = {
        "name": "Feras Al-Aqqad",
        "field": "Backend Developer - Python Django & Django REST Framework",
        "bio": "I am passionate about building scalable APIs and web applications using Django. "
               "I enjoy writing clean code, exploring new technologies, and contributing to open-source projects."
    }
    return Response(data)

# /features → features()
@api_view(['GET'])
def features(request):
    features_list = [
        "Fast Development",
        "Secure",
        "Scalable",
        "Flexible",
        "RESTful APIs"
    ]
    data = {
        "features": features_list
    }
    return Response(data)

# /team → team()
@api_view(['GET'])
def team(request):
    team_members = [
        {"name": "Feras", "role": "Developer"},
        {"name": "Sara", "role": "Designer"},
        {"name": "Nesma", "role": "Project Manager"},
        {"name": "Laila", "role": "QA Tester"}
    ]
    data = {
        "team": team_members
    }
    return Response(data)
