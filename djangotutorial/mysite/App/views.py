from django.shortcuts import render

def grafica_view(request):
    
    '''
    datos para la grafica

    Args:
    request (type): descripcion
    '''

    etiquetas = ['Enero','Febrero','Marzo','Abril','Mayo']

    datos = [5,15,33,24,28]

    return render(request, 'App/Mi_grafica.html' ,{
        'etiquetas_bar' :etiquetas,
        'datos_bar' :datos,

    })
 
def grafica_line_view(request):

    '''

    Datos para la gráfica de líneas

    '''

    etiquetas_line = ['Call of Duty WWI', 'Halo Guardians', 'Battlefield', 'Forza Horizon', 'Hogwarts Legacy']

    datos_line = [250, 230, 189, 200, 180]
 
    return render(request, 'App/Mi_grafica.html', {

        'etiquetas_line': etiquetas_line,

        'datos_line': datos_line,

    })
 
def grafica_pastel_view(request):

    '''

    Datos para la gráfica de pastel

    '''

    etiquetas_pie = ['Intensamente 2', 'Wolverine y Deadpool', 'Mi villano favorito 4', 'Venom Último baile', 'Alien: Romulus']

    datos_pie = [289, 850, 370, 120, 331]
 
    return render(request, 'App/Mi_grafica.html', {

        'etiquetas_pie': etiquetas_pie,

        'datos_pie': datos_pie,

    })
 
def grafica_dispersion_view(request):

    '''

    Datos para la gráfica de dispersión

    '''

    datos_dispersion = [

        {'x': 'Zapatos', 'y': 5},

        {'x': 'Tenis', 'y': 10},

        {'x': 'Tacones', 'y': 5},

        {'x': 'Botas', 'y': 5.5},

        {'x': 'Chanclas', 'y': 8},

    ]
 
    return render(request, 'App/Mi_grafica.html', {

        'datos_dispersion': datos_dispersion,

    })
 
def grafica_histograma_view(request):

    '''

    Datos para la gráfica de histograma

    '''

    etiquetas_histograma = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '80-90', '90-100', '100-110']

    datos_histograma = [5000, 1000, 1500, 8000, 3000, 3000, 3500, 400, 450, 500]
 
    return render(request, 'App/Mi_grafica.html', {

        'etiquetas_histograma': etiquetas_histograma,

        'datos_histograma': datos_histograma,

    })
 
def grafica_boxplot_view(request):

    '''

    Datos para la gráfica de boxplot

    '''

    etiquetas = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo']

    valores = [

        [3, 4, 5, 6, 7],

        [5, 6, 7, 8, 9],

        [4, 5, 6, 7, 8],

        [6, 7, 8, 9, 10],

        [3, 5, 6, 8, 9],

    ]
 
    return render(request, 'App/Mi_grafica.html', {

        'etiquetas_boxplot': etiquetas,

        'datos_boxplot': valores,

    })
