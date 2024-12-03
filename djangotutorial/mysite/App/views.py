from django.shortcuts import render

def grafica_view(request):
    
    '''
    datos para la grafica

    Args:
    request (type): descripcion
    '''

    etiquetas = ['Enero','Febrero','Marzo','Abril','Mayo']

    datos = [5,15,10,20,25]

    return render(request, 'App/Mi_grafica.html' ,{
        'etiquetas_bar' :etiquetas,
        'datos_bar' :datos,

    })
