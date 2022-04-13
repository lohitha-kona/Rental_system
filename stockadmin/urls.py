from django.urls import path,include
from stockadmin import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path("superadmin/",views.adminlogin,name="superadmin"),
	path("adminhome/",views.adminhome,name="adminhome"),

	path("adminaddbook/",views.adminaddbook,name="adminaddbook"),
	path("viewbooks/",views.viewbooks,name="viewbooks"),
	path("deletebooks/<int:id>",views.deletebooks,name="deletebooks"),
	path("updatebooks/<str:book_name>/<str:book_edition>",views.updatebooks,name="updatebooks"),
	path("updatebookdetails/",views.updatebookdetails,name="updatebookdetails"),

	path("addbicycle/",views.addbicycle,name="addbicycle"),	
	path("viewbicycles/",views.viewbicycles,name="viewbicycles"),
	path("deletebicycles/<int:id>",views.deletebicycles,name="deletebicycles"),
	path("updatebicycles/<str:bicycle_name>/<str:bicycle_brand>",views.updatebicycles,name="updatebicycles"),
	path("updatebicycledetails/",views.updatebicycledetails,name="updatebicycledetails"),


	path("adminaddbike/",views.adminaddbike,name="adminaddbike"),	
	path("viewbikes/",views.viewbikes,name="viewbikes"),
	path("deletebikes/<int:id>",views.deletebikes,name="deletebikes"),
	path("updatebikes/<str:bike_name>/<str:bike_model>",views.updatebikes,name="updatebikes"),
	path("updatebikedetails/",views.updatebikedetails,name="updatebikedetails"),



	path("addmanager/",views.addmanager,name="addmanager"),	
	path("viewmanagers/",views.viewmanagers,name="viewmanagers"),
	path("deletemanagers/<int:id>",views.deletemanagers,name="deletemanagers"),


]+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)