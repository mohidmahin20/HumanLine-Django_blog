from django.shortcuts import render,redirect
from . import forms
from .import models
# Create your views here.

def add_post(request):
    if request.method == 'POST': #user post request koreche
        post_form = forms.PostForm(request.POST) #user er post request data ekhane capture korlam
        if post_form.is_valid(): #post kora data gulo valid kina check kortecgi
            post_form.save() #data valid hole databse e save korbo
            return redirect('add_post') #sob thik thakle take add category ei url e pathiye dibo
    else: #user normally website e gele blank form pabe
        post_form= forms.PostForm()
    return render(request,'add_post.html',{'form': post_form})


def edit_post(request,id):
    post= models.Post.objects.get(pk=id)
    post_form = forms.PostForm(instance=post)
    #print(post.title)
    if request.method == 'POST': #user post request koreche
        post_form = forms.PostForm(request.POST,instance=post) #user er post request data ekhane capture korlam
        if post_form.is_valid(): #post kora data gulo valid kina check kortecgi
            post_form.save() #data valid hole databse e save korbo
            return redirect('homepage') #sob thik thakle take add category ei url e pathiye dibo
   
    return render(request,'add_post.html',{'form': post_form})

def delete_post(request,id):
    post= models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')
    