from django.shortcuts import render
from itertools import zip_longest
from core.dp.subsequence import Find_Subsequence
from datetime import datetime
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from core.dp.WeightedIntervalScheduling import *
# Create your views here.

def group_elements(n, iterable, padvalue='x'):
    return zip_longest(*[iter(iterable)]*n, fillvalue=padvalue)

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
    
    return render(request, 'home.html',{'result':longest_sequence})
    
def WIS(request):
    
    postdata = request.POST.dict()
    postdata.pop('csrfmiddlewaretoken')
    
    keysList = list(postdata.values())
    list_quatation = []
    list_quatation = removeQuotation(keysList)

    I = []
    try:
        for output in group_elements(4,list_quatation):
            I.append(output)

        ## CHAMA FUNCAO RESOLVE
        list_resolve = []
        list_resolve = resolve(I)
        
    except ValueError as erro:
        print('entrouexep')
        messages.info(request, 'Por favor certifique se todos os campos foram preenchidos')
        return HttpResponseRedirect('/')

    try:
        weightedinterval = WeightedIntervalScheduling(list_resolve)
        max_weight, best_intervals = weightedinterval.weighted_interval()
    
    except RecursionError as erro:
        messages.info(request, 'A data inicial deve ser menor que o horário final')
        return HttpResponseRedirect('/')
    
    else:
        current_date = datetime.now().date()
        best_intervals = replaceTime(best_intervals)
        print(best_intervals) 
        
    return render(request,'bestintervals.html', {'best_intervals': best_intervals,'current_date': current_date})

