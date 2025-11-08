from django.shortcuts import render, redirect
from lives.forms import CreateFAC, CreateStreamer
from lives.models import Fac, Canal


# Create your views here.
def home_page(request):
    if request.method == 'GET':
        facs = Fac.objects.all()
        canais = Canal.objects.all()
        return render(request, '../templates/home_page.html', {'facs': facs, 'canais': canais})


def add_fac(request):
    if request.method == 'POST':
        form = CreateFAC(request.POST)
        if form.is_valid():
            dados_form = form.data
            item_fac = Fac(nome=form.data['name_fac'])
            item_fac.save()
            return redirect('home_page')


def add_streamer(request):
    if request.method == 'POST':
        form = CreateStreamer(request.POST)
        if form.is_valid():
            dados_form = form.data
            fac = Fac.objects.get(id=dados_form['selectFacPlayer'])
            item_canal = Canal(nome=dados_form['name_canal'], nick_player=dados_form['name_nick'],
                               link_yt=dados_form['name_yt'], link_kick=dados_form['name_kick'],
                               link_tw=dados_form['name_tw'], fac_player=fac)

            item_canal.save()
            return redirect('home_page')


def show_live_fac(request, pk):
    if request.method == 'GET':
        fac = Fac.objects.get(id=pk)
        facs = Fac.objects.all()
        canais = Canal.objects.filter(fac_player=pk)
        print(canais)
        return render(request, '../templates/home_page.html',
                      {'facs': facs, 'fac': fac, 'canais': canais})


def remove_canal(request, pk):
    if request.method == 'GET':
        canal = Canal.objects.get(id=pk)
        canal.delete()
        return redirect('home_page')
