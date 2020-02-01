from django.urls import path
from . import views

#namespace generally give namespaces accoording to your app name
app_name='home'

urlpatterns = [
    path('',views.index1 ),
    path('home/',views.index1,name='index' ),

    path('posts/',views.posts,name='index1' ),
    path('posts/id/<int:keys>',views.post_id,name='post_id' ),

    path('archive/monthly/',views.archive,name='archive'),
    path('archive/yearly/',views.archive_yearly,name='archive_yearly'),
    path('signup/',views.signup1,name='signup' ),
    path('login/',views.login1, name = 'login'),
    path('addpost/',views.addpost,name="addpost"),
    path('logout/',views.logout1,name="logout"),
    path('contactus',views.contactus,name='contactus'),
]