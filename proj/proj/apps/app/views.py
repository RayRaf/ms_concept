from django.shortcuts import render
from .models import Project

# Create your views here.
def projects(request):
    projects_list = Project.objects.all()

    return render(request, 'app/projects.html', {'projects_list': projects_list})




class SpecItem():
    positionaltag = ''
    docsection = ''
    supplier = ''
    product = ''

def project(request, project_id):
    project = Project.objects.get(id = project_id)
    positionaltags_list = project.positionaltag_set.all()
    specitems_list = []
    for p in positionaltags_list:  
        product = p.product
        docsecttion = p.docsection
        supplier = product.supplier

        sp = SpecItem()

        sp.positionaltag = p.tag
        sp.docsection = docsecttion.code_name
        sp.supplier = supplier.supplier_name + ' '+ supplier.supplier_email
        sp.product = product.product_name + ' '+ product.product_name

        specitems_list.append(sp) 



# positionaltag = project.positionaltag_set.all()[:1].get()
#  doc_sections = project.docsection_set.all()
    return render(request, 'app/project.html', {'project': project, 'specitems_list': specitems_list})