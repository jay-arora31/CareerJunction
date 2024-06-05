from django.shortcuts import render
from .forms import *
from django.shortcuts import redirect
from .models import *
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from better_profanity import profanity
from django.contrib import messages

# Create your views here.
def bloghome(request):
    askform=PostForm()
    blogs=Post.objects.all().order_by('post_date').exclude(author__username=request.user)
    tot=TotalData.objects.get(id=1)
    return render(request,'blog/bloghome.html',{'askform':askform,'blogs':blogs,'tot':tot})


def questionpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        print("hey")
        print(form.errors)
        if form.is_valid():
            tot=TotalData.objects.get(id=1)
            tot.total_question+=1
            tot.save()
            text_content = form.cleaned_data['body_content']
            soup = BeautifulSoup(text_content, 'html.parser')
            predictions=profanity.contains_profanity(str(soup))
            print(predictions)
            if predictions==False:
                    print("post is saved")
                    # Save the form data to the database
                    post = form.save()

                    # Redirect to a success page or post detail page
                    return redirect('blog')
            else:
                    messages.success(request, "Please Write Appropriate Word", "alert-danger alert-dismissible")
                    return redirect('blog')
        return redirect('blog')
        
    else:
        # If the form is invalid, re-render it with error messages
            return redirect('blog')



def yourquestion(request):
    posts=Post.objects.filter(author__username=request.user)
    tot=TotalData.objects.get(id=1)
    return render(request,'blog/yourpost.html',{'posts':posts,'tot':tot})


def edit_question(request,id):
    post_data=Post.objects.get(id=id)
    if request.method == 'POST':
        
        print("Heyuwfvweufvwbefbqib",post_data)
        form = PostFormEdit(request.POST,instance=post_data)
        print(form.errors)
        if form.is_valid():
             print("Hey2111111")
             form.save()
             return redirect('yourquestion')
    form = PostFormEdit(instance=post_data)
    id=id
    return render(request,'blog/edit_question.html',{'form':form,'id':id})
     

def answer_question(request,id):
    post_data=Post.objects.get(id=id)
    user_obj=User.objects.get(username=request.user)
    if request.method == 'POST':
            tot=TotalData.objects.get(id=1)
            tot.total_answer+=1
            tot.save()
            post_data.answercount+=1
            post_data.save()
            answer=request.POST['answer']
            ans_obj=AnswerQuestion(body_content=answer,post=post_data,user=user_obj)
            ans_obj.save()
            return redirect('answer_question',id)
    post_data=Post.objects.get(id=id)
    post_data.viewcount+=1
    answers=AnswerQuestion.objects.filter(post__id=id).order_by('answer_date').reverse()
    print(answers)
    tot=TotalData.objects.get(id=1)
    return render(request,'blog/answer.html',{'post_data':post_data,'answers':answers,'id':id,'tot':tot})
     



def like_button(request,id):
    post=Post.objects.get(id=id)
    user=User.objects.get(username=request.user)
    data=PostLike.objects.filter(post=post,user=user)
    if data:
         return redirect('blog')
    else:
        data_obj=PostLike(post=post,user=user)
        data_obj.save()
        post.likecount+=1
        post.save()
        return redirect('blog')
    


def dislike_button(request,id):
    post=Post.objects.get(id=id)
    user=User.objects.get(username=request.user)
    data=PostDislike.objects.filter(post=post,user=user)
    if data:
         return redirect('blog')
    else:
        data_obj=PostDislike(post=post,user=user)
        data_obj.save()
        post.unlikecount+=1
        post.save()
        return redirect('blog')
    


def most_answer_question(request):
    askform=PostForm()
    blogs=Post.objects.all().order_by('answercount').reverse()
    tot=TotalData.objects.get(id=1)
    return render(request,'blog/bloghome.html',{'askform':askform,'blogs':blogs,'tot':tot})

def unanswer_question(request):
    askform=PostForm()
    blogs=Post.objects.filter(answercount=0)
    tot=TotalData.objects.get(id=1)
    return render(request,'blog/bloghome.html',{'askform':askform,'blogs':blogs,'tot':tot})


def search_by_category(request):
    cate=request.GET.get('category')
    askform=PostForm()
    blogs=Post.objects.filter(category=cate)
    tot=TotalData.objects.get(id=1)
    return render(request,'blog/bloghome.html',{'askform':askform,'blogs':blogs,'tot':tot})
