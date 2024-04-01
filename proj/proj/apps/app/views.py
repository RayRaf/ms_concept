from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import DocSection, Project
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Create your views here.
def projects(request):
    projects_list = Project.objects.all()

    return render(request, 'app/projects.html', {'projects_list': projects_list})




class SpecItem():
    positionaltag = ''
    docsection = ''
    supplier = ''
    product = ''
    product_order_code = ''
    product_manufacturer = ''
    product_amount = ''
    product_amount_unit = ''
    num = ''


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


def sendmail(request):
    try:
        # create message object instance 
# import necessary packages 
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        import smtplib
        # create message object instance 
        msg = MIMEMultipart()
        message = "Тестовое письмо. Отправлено при помощи Python Django"
        # setup the parameters of the message 
        password = "****"
        msg['From'] = "mail@rayraf.ru"
        msg['To'] = "rayraf@mail.ru"
        msg['Subject'] = "Test message"
        # add in the message body 
        msg.attach(MIMEText(message, 'plain'))
        #create server 
        server = smtplib.SMTP('smtp.yandex.ru', 587, timeout=10)
        server.starttls()
        # Login Credentials for sending the mail 
        server.login(msg['From'], password)
        # send the message via the server. 
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        print ("successfully sent email to %s:" % (msg['To']))
        
        return HttpResponse('Удачно!')
    except:
        raise Http404('Не удалось отправить сообщение')
    
def specprintdemo(request):
    return render(request, 'app/specprintdemo.html')




def docsectionspec(request, project_id, section):
    project = Project.objects.get(id = project_id)
    sec = DocSection.objects.get(code_name = section)
    positionaltags_list = project.positionaltag_set.filter(docsection = sec)
    print(positionaltags_list)
    specitems_list = []
    


    for p in positionaltags_list:  
        product = p.product
 
        sp = SpecItem()

        sp.positionaltag = p.tag
        sp.product = product.product_name 
        sp.product_order_code = product.product_order_code
        sp.product_manufacturer = product.product_manufacturer


        specitems_list.append(sp) 
        

    return render(request, 'app/docsection.html', {'project': project, 'specitems_list': specitems_list, 'section': section})
 

def specprint(request, project_id, section):
    project = Project.objects.get(id = project_id)
    sec = DocSection.objects.get(code_name = section)
    positionaltags_list = project.positionaltag_set.filter(docsection = sec)
    print(positionaltags_list)
    specitems_list = []
    num = 2


    for p in positionaltags_list:  
        product = p.product

        sp = SpecItem()

        sp.positionaltag = p.tag
        sp.product = product.product_name 
        sp.product_order_code = product.product_order_code
        sp.product_manufacturer = product.product_manufacturer
        sp.num = 'line'+str(num)


        specitems_list.append(sp) 
        num+=1

    return render(request, 'app/specprint.html', {'project': project, 'specitems_list': specitems_list, 'section': section})