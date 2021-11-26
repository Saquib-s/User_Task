
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import user_model
from .serilizer import User_Serializer

# Create your views here.
class User_view(APIView):
    def post(self, request):
        user_data = User_Serializer(data=request.data)
        if user_data.is_valid():
            user_data.save()
            return Response(user_data.data)
        else:
            return Response("not exists")

    def get(self,request):
        dept_data = user_model.objects.all()
        serializer = User_Serializer(dept_data,many=True)
        return Response(serializer.data)


class check_size(APIView):
    def get(self,request,image):
        image.seek(0, 2)
        size = image.tell()
        if int(size) > int(Config.Image_Size):
            return False
        return True


class get_client_ip(APIView):
    def get(self,request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip





