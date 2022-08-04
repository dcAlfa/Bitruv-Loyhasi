from django.shortcuts import render
from django.views import View
from .models import  *


class ClubsView(View):
    def get(self, request):
        clubs = Club.objects.all()
        davlats = Davlat.objects.all()
        data = {
            "davlatlar": davlats,
            "clublar": clubs
        }
        return render(request,"clubs.html",data)

class AboutView(View):
    def get(self, request):
        davlats = Davlat.objects.all()
        data = {
            "davlatlar": davlats
        }
        return render(request,"about.html",data)

class AsosiyView(View):
    def get(self, request):
        davlats = Davlat.objects.all()
        data = {
            "davlatlar": davlats
        }
        return render(request,"index.html", data)

class ClubView(View):
    def get(self, request):
        davlats = Davlat.objects.all()
        data = {
            "davlatlar": davlats
        }
        return render(request,"club.html",data)

class OxirgiView(View):
    def get(self, request):
        davlats = Davlat.objects.all()
        transfer = Transfer.objects.filter(mavsum="22/23")
        print(transfer)
        data = {
            "davlatlar": davlats,
            "transferlar": transfer
        }
        return render(request,"latest-transfers.html",data)

class PlayersView(View):
    def get(self, request):
        players = Player.objects.all()
        davlats = Davlat.objects.all()
        data = {
            "davlatlar": davlats,
            "playerlar": players
        }
        return render(request,"players.html",data)

class RecordsView(View):
    def get(self, request):
        davlats = Davlat.objects.all()
        transfer = Transfer.objects.filter(narx__gte=50)
        data = {
            "davlatlar": davlats,
            "transferlar": transfer
        }
        return render(request,"records.html",data)

class SezonView(View):
    def get(self, request):
        davlats = Davlat.objects.all()
        data = {
            "davlatlar": davlats
        }
        return render(request,"season.html",data)

class StatsView(View):
    def get(self, request):
        davlats = Davlat.objects.all()
        data = {
            "davlatlar": davlats
        }
        return render(request,"stats.html",data)

class TransferView(View):
    def get(self, request):
        davlats = Davlat.objects.all()
        transfer = Transfer.objects.all()
        data = {
            "davlatlar": davlats,
            "transferlar": transfer
        }
        return render(request,"transfer.html",data)

class UrinishView(View):
    def get(self, request):
        davlats = Davlat.objects.all()
        data = {
            "davlatlar": davlats
        }
        return render(request,"tryouts.html",data)

class U20PlayerView(View):
    def get(self, request):
        players = Player.objects.filter(yosh__lte=20).order_by("-narx")
        davlats = Davlat.objects.all()
        data = {
            "davlatlar": davlats,
            "playerlar": players
        }
        return render(request,"U20-players.html",data)

class DavlatView(View):
    def get(self,request,pk):
        davlat = Davlat.objects.get(id = pk)
        davlatlar = Davlat.objects.all()
        club = Club.objects.filter(davlat=davlat)
        data = {
            "clublar":club,
            'davlat': davlat,
            "davlatlar": davlatlar
        }
        return render(request, "davlatlar.html", data)







