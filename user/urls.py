from django.urls import path,include
from user import views
from django.conf import settings
from django.conf.urls.static import static
from project.settings import MEDIA_ROOT, MEDIA_URL



urlpatterns = [

	path("registration/",views.registration,name="registration"),
	path("userlogin/",views.userlogin,name="userlogin"),
	path("userchecklogin/",views.userchecklogin,name="userchecklogin"),
	path("userhome/",views.userhome,name="userhome"),


	path("rentabook/",views.rentabook,name="rentabook"),
	path("renting/<int:book_id>/<str:book_name>/<int:book_cost>/<int:book_stock>",views.renting,name="renting"),
	#path("rentcheck/<int:book_id>/<int:book_stock>",views.rentcheck,name="rentcheck"),


	path("rentabicycle/",views.rentabicycle,name="rentabicycle"),
	path("renting2/<int:bicycle_id>/<str:bicycle_name>/<int:bicycle_cost>/<int:bicycle_stock>",views.renting2,name="renting2"),



	path("rentabike/",views.rentabike,name="rentabike"),
	path("rentingbike/<int:bike_id>/<str:bike_name>/<int:bike_cost>/<int:bike_stock>",views.rentingbike,name="rentingbike"),


]+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
