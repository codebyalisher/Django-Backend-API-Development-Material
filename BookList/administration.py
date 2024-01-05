from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

@api_view()
@permission_classes([IsAuthenticated])  # Note the square brackets to create a list
def secret(request):
    return Response({'Message': 'save secret message'})

@api_view(['GET'])  # Specify the allowed HTTP methods, e.g., 'GET'
@permission_classes([IsAuthenticated])  
def manager_view(request):
    if request.user.groups.filter(name='Manager').exists():
        return Response({'Message': 'This Manager should see the message only'})
    else:
        return Response({'Message': 'You are not authorized'})
