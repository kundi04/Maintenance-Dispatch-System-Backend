from django.contrib.auth import authenticate, login, logout, get_user_model
from django.middleware.csrf import get_token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

User = get_user_model()


class GetCSRFToken(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        token = get_token(request)
        return Response({'csrfToken': token})


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({
                'message': 'Login successful',
                'role': user.role,
                'username': user.username,
                'csrfToken': get_token(request),
            })

        return Response({'error': 'Invalid credentials'}, status=400)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'Logged out'})


class MeView(APIView):
    def get(self, request):
        return Response({
            'username': request.user.username,
            'role': request.user.role
        })


class StaffListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role != 'manager':
            return Response({'error': 'Not authorized'}, status=403)
        
        staff_users = User.objects.filter(role='staff')
        return Response([
            {'id': user.id, 'username': user.username}
            for user in staff_users
        ])
