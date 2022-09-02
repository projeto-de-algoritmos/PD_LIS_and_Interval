from django.shortcuts import render
from core.dp.subsequence import Find_Subsequence
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def home_view(request):

    
    return render(request, 'home.html')

def LIS(request):
    try:
        values = request.POST.get('lis')
        remove_quotation = list(values.split(","))
        list_to_sequence = [int(i) for i in remove_quotation]
        n = len(list_to_sequence)
    
        longest_sequence = Find_Subsequence(list_to_sequence,n)
        print(longest_sequence)
    except:
        messages.info(request, '')
        return HttpResponseRedirect('/')  
    
    return render(request, 'modalLIS.html',{'result':longest_sequence})
    

