from django.urls import path
from msg import views
from msg.views import ContactForm
'''
For function base views:
    path('urlpattren',views.functionname())
For class base view:
    path('urlpattern',classname.as_view()) 
'''
urlpatterns = [
    path ('contact/<sid>',ContactForm.as_view()),
    path('about',views.about),
    path('edit/<id>',views.edit),
    path('hello',views.hello),
    path('base',views.base),
    path('inheritance',views.inheritance),
    path('message',views.msg),
    path('dashboard',views.dashboard),
    path('delete/<did>',views.delete),
]