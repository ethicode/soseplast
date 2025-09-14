from django.shortcuts import render
from .models import MyUser
# Create your views here.
def liste_utilisateurs(request):
    utilisateurs = MyUser.objects.all()
    return render(request, 'utilisateurs/liste_utilisateurs.html', { 'utilisateurs': utilisateurs })


def detail_utilisateur(request, pk):
    utilisateur = MyUser.objects.get(pk=pk)
    return render(request, 'utilisateurs/detail_utilisateur.html', {'utilisateur': utilisateur})