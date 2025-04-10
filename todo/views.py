from django.shortcuts import render, redirect
from .models import Gasto
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        cantidad = request.POST.get('cantidad')
        if descripcion and cantidad:
            Gasto.objects.create(descripcion=descripcion, cantidad=cantidad)
            return redirect('home')
    gastos = Gasto.objects.all().order_by('-fecha')
    total = sum(g.cantidad for g in gastos)
    return render(request, 'todo/home.html', {'gastos': gastos, 'total': total})
