from django.shortcuts import render
from .models import *
# Create your views here.


def roadmapList(request):
    roadmaps=Roadmap.objects.all()

    
    return render(request,'roadmap/roadmaplist.html',{'roadmaps':roadmaps})

def roadmapDetail(request,roadmap_slug):
    data=Roadmap.objects.get(roadmap_slug=roadmap_slug)
    topic_data=Topic.objects.filter(roadmap=data)
    result_dict={}
    subtopic_dict=[]
    for i in topic_data:
        temp=[]
        subtopic_data=Subtopic.objects.filter(roadmap=data,topic=i)
        for i in subtopic_data:
            temp.append(i)
        

        result_dict[i.subtopic_name]=temp

    print(result_dict)



    for keys,values in result_dict.items():
        for j in values:
            print(j.subtopic_link)

    return render(request,'roadmap/roadmapdetail.html',{'result_dict':result_dict})
