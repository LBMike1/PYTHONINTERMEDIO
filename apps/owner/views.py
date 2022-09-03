from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from apps.owner.forms import OwnerForm
from apps.owner.models import Owner

from django.db.models import Q, F

from django.views.generic import ListView, CreateView, UpdateView, DeleteView


def owner_list(request):
    # data_context = {'nombre_owner': 'KEVIN',
    #                 'edad': 18,
    #                 'pais': 'Perú',
    #                 'vigente': False,
    #                 'pokemones': [{
    #                                 'nombre_pokemon': "Charizard",
    #                                 'ataques': ['atq 1 Charizard', 'atq 2 Charizard','atq 3 Charizard']
    #                             },
    #                             {
    #                                 'nombre_pokemon': "New",
    #                                 'ataques': ['atq 1 New', 'atq 2 New', 'atq 3 New']
    #                             },
    #                             {
    #                                 'nombre_pokemon': "Balbasour",
    #                                 'ataques': ['atq 1 Balbasour', 'atq 2 Balbasour', 'atq 3 Balbasour']
    #                             }
    #                             ]
    #                 }

    """Crear un objeto en la Base de Datos"""
    #p = Owner(nombre="Rousmery", edad=37)
    #p.save()

    #p.nombre = "Karla"
    #p.save()

    """Obtener todos los datos de una tabla en la BD"""
    # data_context = Owner.objects.all()

    """Filtración de datos: filter()"""
    #data_context = Owner.objects.filter(nombre='Karla')

    """Filtración de datos con AND de SQL: filter()"""

    #data_context = Owner.objects.filter(nombre='Karla', edad='29')

    """Filtración de datos más preciosos con: __constains"""

    #data_context = Owner.objects.filter(nombre__contains='karla')

    """Filtración de datos más preciosos con: __endswith"""
    #data_context = Owner.objects.filter(nombre__endswith='la')

    """Ordenar por cualquier atributo en la Base de Datos"""

    """Ordenar alfabéticamente por nombre"""
    #data_context = Owner.objects.order_by('nombre')

    """Ordenar alfabéticamente por edad"""
    #data_context = Owner.objects.order_by('edad')

    """Ordenar de manera inversa por la edad"""
    data_context = Owner.objects.order_by('-edad')

    """Acortar datos: Obtener un rango de registro de una tabla en la BD"""
    #data_context = Owner.objects.all()[2:6]

    """Eliminar objetos en la BD"""
    """Eliminar el objeto con id = 31 en la BD"""
    #p = Owner.objects.get(id=11)
    #p.delete()

    """Eliminando un conjunto de datos específico"""
    # Owner.objects.filter(pais__startswith="Bra").delete()

    """Eliminar todos los objetos de la BD"""
    #p = Owner.objects.all()
    #p.delete()

    """Actualización de datos en la BD a un cierto un grupo de datos"""

    #Owner.objects.filter(pais__startswith="Bra").update(edad=17)

    """Concatenar consultas"""
    #data_context = Owner.objects.filter(nombre="Karla").order_by("-edad")

    """Utilizando F expressions"""

    #Owner.objects.filter(edad__gte=17).update(edad=F('edad') + 10)

    #data_context = Owner.objects.get(nombre="Karla")

    """Consultas complejas"""

    query = Q(pais__startswith='Pe') | Q(pais__startswith='Br')

    "Negar Q"
    #query = Q(pais__startswith='Pe') & ~Q(edad=37)

    #print("Query: {}".format(query))
    # Query

    #data_context = Owner.objects.filter(query)

    #query = Q(pais__startswith='Pe') | Q(pais__startswith='Br')

    # Query inválida
    "Error de consulta Q"
    #data_context = Owner.objects.filter(edad=37, query)

    #data_context = Owner.objects.filter(query, edad=37)

    return render(request, 'owner/owners.html', context={'data': data_context})


def owner_details(request):

    return render(request, 'owner/owner_detail.html', {})


def owner_search(request):
    query = request.GET.get('q', '')
    #print("query: {}".format(query))
    results = (
        Q(nombre__icontains=query)
    )
    print("resuts: {}".format(results))
    data_context = Owner.objects.filter(results).distinct()

    return render(request, 'owner/owner_search.html', context={'data': data_context, "query": query})


def owner_create(request):
    if request.method == "POST":
        form = OwnerForm(request.POST)
        if form.is_valid():
            """Guarda todos los campos que vienen desde la plantilla"""
            # nombre = form.cleaned_data['nombre']
            # print("Nombre: {}".format(nombre))
            # edad = form.cleaned_data['edad']
            # pais = form.cleaned_data['pais']
            try:
                form.save()
                return redirect('owner_list')
            except:
                pass
    else:
        form = OwnerForm()

    return render(request, 'owner/owner-create.html', {'form': form})


def owner_delete(request, id):
    owner = Owner.objects.get(id=id)
    owner.delete()
    return redirect('owner_list')


def owner_edit(request, id):
    owner = Owner.objects.get(id=id)
    form = OwnerForm(initial={'nombre': owner.nombre, 'edad': owner.edad, 'pais': owner.pais})

    if request.method == 'POST':
        form = OwnerForm(request.POST, instance=owner)
        if form.is_valid():
            try:
                form.save()
                return redirect('owner_list')
            except:
                pass
    return render(request, 'owner/owner_update.html', {'form': form})


""" Vistas basadas en clases """
""" ListView, CreateView, UpdateView, DeleteView """


class OwnerList(ListView):
    model = Owner
    template_name = 'owner/owner_vc.html'


class OwnerCreate(CreateView):
    model = Owner
    form_class = OwnerForm
    template_name = 'owner/owner-create.html'
    success_url = reverse_lazy('owner_list_vc')


class OwnerUpdate(UpdateView):
    model = Owner
    form_class = OwnerForm
    template_name = 'owner/owner_update_vc.html'
    success_url = reverse_lazy('owner_list_vc')


class OwnerDelete(DeleteView):
    model = Owner
    template_name = 'owner/owner-confirm-delete.html'
    success_url = reverse_lazy('owner_list_vc')
