from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
    #return HttpResponse('''
    #<a href = "https://data-flair.training/blogs/python-built-in-functions/">codeee</a>
    #''')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc','off')
    newline = request.POST.get('newline','off')
    capital = request.POST.get('Capitalize', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')
    print(djtext)
    if removepunc =='on':
        punctuations = '''!@#$%^&*()_=:;<>?''""/|\,.'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        djtext = analyzed
        params = {'purpose':'remove punctuations', 'analyze_text':analyzed}
        return render(request,'analyze.html', params)
    if capital == 'on':
        analyzed =djtext.upper()
        djtext = analyzed
        params = {'purpose': 'String capitalize', 'analyze_text': analyzed}
        return render(request, 'analyze.html', params)
    if newline == 'on':
        analyzed =''
        for char in djtext:
            if char!= '\n' and char!='\r':
                analyzed += char
        djtext = analyzed
        params = {'purpose': 'New Line Break', 'analyze_text': analyzed}
        return render(request, 'analyze.html', params)
    if extraspaceremove == 'on':
        analyzed =''
        for index,char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==" "):
                analyzed += char
        djtext = analyzed
        params = {'purpose': 'Extra Space Remove', 'analyze_text': analyzed}
        return render(request, 'analyze.html', params)
    if charcount == 'on':
        count = len(djtext)
        analyzed = "The length of string is "+str(count)
        djtext = analyzed
        params = {'purpose': 'Character Count', 'analyze_text': analyzed}
        return render(request, 'analyze.html', params)
    if charcount =='off' and extraspaceremove == 'off' and newline == 'off' and capital == 'off' and removepunc == 'off':
        return HttpResponse("Please select a analyzed tool.")


def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')