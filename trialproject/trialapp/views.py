from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import projects
from .forms import ProjectForm



profiles = [
    {
        "id": "1",
        "name": "Cody Seibert",
        "description": "I'm a full stack web developer who probably spends too much time coding. A core contribute to the Mumble project and online instructor."
    },
    {
        "id": "2",
        "name": "Dennis Ivy",
        "description": "I build new projects just to tickle my brain and love teaching others how they're made. While I keep busy teaching courses, I still take interviews in search of a great team & projects that interest me."
    },
    {
        "id": "3",
        "name": "Mehdi",
        "description": " I am a Full-Stack Developer.  I am Currently learning, working my skills in web development. Open source enthusiast"
    },
    {
        "id": "4",
        "name": "Cody Seibert",
        "description": "I'm a full stack web developer who probably spends too much time coding. A core contribute to the Mumble project and online instructor."
    },
    {
        "id": "5",
        "name": "Mohammad Khaled",
        "description": "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia"
    },
    {
        "id": "6",
        "name": "Praveen",
        "description": " I’m currently working on - Python, Django, Vue, Nuxt. I’m currently learning - Nodejs.  I’m looking to collaborate with - Any Business or Open Source Idea. Ask me about - Freelancing , Python , Django, Vuejs."
    },]

def mainproject(request):
    msg=' you are on the project page'
    number=11
    project=projects.objects.all()
    print(project)
    context={'message':msg,'number':number,'profiles':profiles,'project':project}
    return render(request,'projectpage/Main_project.html',context)

def project(request,pk):
    projectObj=projects.objects.get(id=pk)
    # tags=projectObj.tags.all()
    return render(request,'projectpage/project.html',{'project':projectObj})

def project_two(request,pk):
    
    return HttpResponse('Hello'+pk)

def Createproject(request):
    form=ProjectForm()
    if request.method=='POST':
        form=ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mainproject')

    context={'form':form}
    return render(request,'projectpage/project_form.html',context)


def Updateproject(request,pk):
    project=projects.objects.get(id=pk)
    form=ProjectForm(instance=project)
    if request.method=='POST':
        form=ProjectForm(request.POST,request.FILES,  instance=project)
        if form.is_valid():
            form.save()
            return redirect('mainproject')

    context={'form':form}
    return render(request,'projectpage/project_form.html',context)


def deleteproject(request,pk):
    project=projects.objects.get(id=pk)
    if request.method=="POST":
        project.delete()
        return redirect('mainproject')
    context={'object':project}


    context={'form':project}
    return render(request,'projectpage/delete_object.html',context)