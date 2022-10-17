from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, permission_required
from empleado.forms import EmpleadoEdit, EmpleadoForm
from django.contrib import messages
from admin_hostal.models import Empleado

@login_required(login_url='/login/')   
def empleados(request):
    Empleados = Empleado.objects.all()
    print(Empleados)
    return render(request, 'index_emp.html', {'Empleados' : Empleados})

@login_required(login_url='/login/')
def crearEmp(request):
    formulario = EmpleadoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'El Empleado fue creado correctamente.')
        return redirect('empleado:empleados')
            
    return render(request, 'crear_emp.html', {'formulario': formulario})

@login_required(login_url='/login/')
def editarEmp(request, id):
    empleados = Empleado.objects.get(id_empleado=id)
    formulario = EmpleadoEdit(request.POST or None, request.FILES or None, instance=empleados)
    if formulario.is_valid() and request.POST:
        formulario.save()
        messages.success(request, 'El Empleado fue modificado correctamente.')
        return redirect('empleado:empleados')
    return render(request, 'editar_emp.html', {'formulario': formulario})

@login_required(login_url='/login/')
def eliminarEmp(request, id):
    empleados = Empleado.objects.get(id_empleado=id)
    if empleados.delete():
        messages.warning(request, 'El Empleado fue Eliminado correctamente.')
        return redirect('empleado:empleados')
    else:
        messages.error(request, 'Algo salió mal.')
        return redirect('empleados')

