# this file create by me

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def analyze(request):
    # get the text from html forms
    djtext=request.POST.get('text','default')

    # cheek Check values
    # removepunc=request.GET.get('removerpunc','off')
    # fullcaps=request.GET.get('fullcaps','off')
    # newlineremover=request.GET.get('newlineremover','off')
    # spaceremover=request.GET.get('spaceremover','off')
    # charcounter=request.GET.get('charcounter','off')
    """I am use post request to clear and look god my urls"""

    removepunc=request.POST.get('removerpunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    spaceremover=request.POST.get('spaceremover','off')
    charcounter=request.POST.get('charcounter','off')
    
    #function to remover the punctuation from the text 
    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyze=""
        for char in djtext:
            if char not in punctuations:
                analyze=analyze+char
        params={'purpose':'Remove Punctuation','analyzed_text':analyze}
        # Analize the text
        return render(request,'analyze.html',params)
    
    #Function to convert in to upper case
    elif fullcaps=="on":
        analyze="" 
        for char in djtext:
            analyze=analyze+char.upper()
        params={'purpose':'Upper case','analyzed_text':analyze}
        return render(request,'analyze.html',params)
    
    # functon to remover the new line
    elif newlineremover=="on":
        analyze=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyze=analyze+char
        params={'purpose':"Remove new line",'analyzed_text':analyze}
        return render(request,'analyze.html',params)
    
    #space remover 
    elif spaceremover=="on":
        analyze=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyze=analyze+char

        
        params={'purpose':"Space Remover",'analyzed_text':analyze}
        return render(request,'analyze.html',params)
    
    # this is char counter
    elif charcounter=="on":
        sum=0
        for char in djtext:
            if char != ' ' and char != '\n':
                sum+=1 
        params={'purpose':"char counnter",'Total':'Total nmber of char is:','analyzed_text':sum}
        return render(request,'analyze.html',params)

    # else condtion to not throw the down time 
    else:
        return HttpResponse("Error try to fix it")
