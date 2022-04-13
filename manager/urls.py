from django.urls import path,include
from manager import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
	path("managerlogin/",views.managerlogin,name="managerlogin"),
	path("managerhome/",views.managerhome,name="managerhome"),

	path("addstaff/",views.addstaff,name="addstaff"),	
	path("viewstaff/",views.viewstaff,name="viewstaff"),
	path("deletestaff/<int:id>",views.deletestaff,name="deletestaff"),


	path("viewbookorders/",views.viewbookorders,name="viewbookorders"),	
	path("updatebookorders/<int:order_id>",views.updatebookorders,name="updatebookorders"),

	path("viewbicycleorders/",views.viewbicycleorders,name="viewbicycleorders"),	
	path("updatebicycleorders/<int:order_id>",views.updatebicycleorders,name="updatebicycleorders"),

	path("viewbikeorders/",views.viewbikeorders,name="viewbikeorders"),	
	path("updatebikeorders/<int:order_id>",views.updatebikeorders,name="updatebikeorders"),

	path("mviewdeliveries/",views.mviewdeliveries,name="mviewdeliveries"),
	path("mviewreturns/",views.mviewreturns,name="mviewreturns"),



]+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)