from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views import generic
from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .forms import UserForm
from .models import Music
from .serializers import musicSerializer
'''
def index(request):
    return HttpResponse("<h1>This is trial page</h1>")
'''
@api_view(['GET', 'POST'])
def MusicList(request):
    if request.method=="GET":
        musics=Music.objects.all()
        serializer=musicSerializer(musics,many=True)
        return Response(serializer.data)

    elif request.method=="POST":
        serializer=musicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def MusicDetails(request,pk):
    try:
        music=Music.objects.get(pk=pk)
    except Music.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method=="GET":
        musics=musicSerializer(music)
        return Response(musics.data)

    elif request.method=="PUT":
        musics=musicSerializer(music,data=request.data)
        if musics.is_valid():
            musics.save()
            return Response(musics.data)
        return Response(musics.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method=="DELETE":
        music.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserFormView(View):
    form_class=UserForm
    template_name='music/registration_form.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():
            user=form.save(commit=False)
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.save(username,password)



