from django.urls import path,include
from staff import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
	path("stafflogin/",views.stafflogin,name="stafflogin"),

	path("staffhome/",views.staffhome,name="staffhome"),

	
	path("viewtaskscompleted/",views.viewtaskscompleted,name="viewtaskscompleted"),
	path("viewdeliveries/",views.viewdeliveries,name="viewdeliveries"),
	path("viewreturns/",views.viewreturns,name="viewreturns"),

	path("delivered/<int:order_id>",views.delivered,name="delivered"),
	path("returned/<int:order_id>",views.returned,name="returned"),


]+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)