from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from .models import User
import jwt, datetime





class Loginview(APIView):
    def post(self, request):
        email = request.data['emamil']
        password = request.data['password']

        User.object.filter(email=email).first()
        if User is None:
            raise APIException('user not found')
        if not User.check_password(password):
            raise APIException('Incorrect Password')
        
        payload = {
            'id': User.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
        response = Response()

        response.set_cookie(key='jwt', value='token', httponly=True)
        response.data = {
            'jwt': token
        }
        return response
    


class Userview(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise APIException ('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise APIException ('Unauthenticated!')
        user = User.objects.filter(id = payload['id']).first()
        serializer = UserSerializer(user)

        return Response (serializer.data)
    
class Logoutview(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message' : 'success'
        }

        return response


class Registerview(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    


#     if request.method == "POST" :
#         form  = UserRegisterForm(request.POST or None)
#         if form.is_valid():
#             new_user = form.save()
#             username = form.cleaned_data.get('username')
#             messages.success('request', 'Created successfully')
#             new_user = authenticate(username = form.cleaned_data['email'], 
#                                     password = form.clean_data['password1']
#                                     )
#             login(request, new_user)
#             return redirect('FullStock_traders:index')
    
#     else:
#         print("Registration failed")
    
    
# #The context helps us to display the form
#     context = {
#         'form' : form,
#     }

# #have to create a template with the Authentication/SignUP.html
#     return render(request, 'Authentication/signUp.html', context)

