# this is created by me

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
       return render(request,'index.html')

def removepunc(request):
    #get the text
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover','off')
    spaceremover = request.GET.get('spaceremover','off')
    onlyoneline = request.GET.get('onlyoneline','off')
    charcounter = request.GET.get('charcounter','off')
    print(removepunc)
    if removepunc == "on":
        PUNCTUATION ='''/[-[\]{}()*+?.;,\\'^$|#\]/,"\\$&"'''
        analyzed = ""
        for char in djtext:
            if char not in PUNCTUATION:
                analyzed = analyzed + char

        params ={'purpose':'remove punctuatuions','analyze_text':analyzed}
        #analyze the text
        return render(request,'analyze.html',params)

    elif(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed = analyzed+char.upper()

        params = {'purpose': 'change to uppercase', 'analyze_text': analyzed}
        return render(request,'analyze.html',params)

    elif(newlineremover == "on"):
        analyzed=""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'remove new lines', 'analyze_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(spaceremover=="on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not (djtext[index] == ' ' and djtext[index+1]==' '):
                analyzed = analyzed + char

        params = {'purpose': 'remove the space', 'analyze_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (onlyoneline == "on"):
        analyzed = ""
        for char in djtext:
            if char == '\n':
                break
            else:
                analyzed = analyzed + char

        params = {'purpose': 'remove new lines', 'analyze_text': analyzed}
        return render(request, 'analyze.html', params)


    elif (charcounter == "on"):
        analyzed = ""
        for char in djtext:
            if char != 'null':
                analyzed = analyzed + char

        params = {'purpose': 'remove new lines', 'analyze_text': len(analyzed)}
        return render(request, 'analyze.html', params)


    else:
        return HttpResponse("error")


