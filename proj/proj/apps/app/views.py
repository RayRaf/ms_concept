from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import DocSection, Project, Product
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Create your views here.
def projects(request):
    projects_list = Project.objects.all()

    return render(request, 'app/projects.html', {'projects_list': projects_list})




class SpecItem():
    id = 0
    positionaltag = ''
    docsection = ''
    supplier = ''
    product = ''
    product_order_code = ''
    product_manufacturer = ''
    product_amount = 1
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
        sp.product = product.product_name + ' '+ product.product_order_code
        sp.id = product.id


        specitems_list.append(sp) 




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
        sp.id = product.id


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








    specitems_list_consolidated = []
    for sl in specitems_list:
        cnt = 0
        for sc in specitems_list_consolidated:
            if sc.product_order_code == sl.product_order_code:
                cnt +=1
        if cnt == 0:
            specitems_list_consolidated.append(sl)
     
        



    for s1 in specitems_list_consolidated:
        cnt = 0
        for s2 in specitems_list:
            if s1.product_order_code == s2.product_order_code:
                cnt += 1
                if s1.positionaltag != s2.positionaltag:
                    s1.positionaltag = s1.positionaltag + ', '+ s2.positionaltag
        s1.product_amount = cnt






    num = 2
    for s in specitems_list_consolidated:
        s.num = 'line'+str(num)
        num+=1
        print(s.product_amount)

    return render(request, 'app/specprint.html', {'project': project, 'specitems_list_consolidated': specitems_list_consolidated, 'section': section})



def product_properties(request, product_id):
    p = Product.objects.get(id = product_id)

    property_values_list = p.property_value_set.order_by('id')

    return render(request, 'app/product.html', {'product': p, 'property_values_list': property_values_list})