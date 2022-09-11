from django.urls import path
from . import views
import random

urlpatterns = [
	path('',views.home,name='home'),
	path('gallery',views.gallery,name='gallery'),
	path('signup/',views.signup,name='signup'),
	path('login/',views.login,name='login'),
	path('logout/',views.logout,name='logout'),
	path('createpassword/',views.createpassword,name='createpassword'),
	path('lock/',views.lock,name='lock'),
	path('originalgalleryas1h2jk46ckf9l30y3j8hj28jd73k8j4n9j3kv93jv3j03jhdgj8dgh3ikr9gen3jh43h43n5j4l654l54353n53h34i35lh3433h4iho3h4o3ho4p3h4i43ol45ho34n33ho3j4o3j43o4h3h43h4o3h4o3h4o3h4o3h4o34o3h4o3h4oh3o4h3o4o34h3oh43oh4o3o34ho3h43434h3o434343o33h4o3h4o3h34h34h3oh4o3h4o3h4o3h43oh43oh43',views.originalgallery,name='originalgallery'),
	path('editpassword/',views.editpassword,name='editpassword'),


]