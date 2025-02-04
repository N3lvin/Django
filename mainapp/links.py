from .views import homepage, aboutus ,contactpage,pricingpage,login,fetch_allusers,create_songs,fetch_allsongs,fetch_onesong,fetch_oneuser,edit_song,edit_user,delete_user,delete_onesong,create_record,sign_in,sign_up
from django.urls import path

urlpatterns=[
    path("homepage/", view =homepage, name="homepage"),
    path("aboutus/", view=aboutus, name="aboutus"),
    path("contactpage/",view=contactpage, name="contactpage"),
    path("pricingpage/",view=pricingpage, name="pricingpage"),
    path("loginpage/",view=login,name="loginpage"),
    path("fetch_allusers",view=fetch_allusers,name="fetch_allusers"),
    path("create_songs",view=create_songs,name="create_songs"),
    path("fetch_allsongs",view=fetch_allsongs,name="fetch_allsongs"),
    path("fetch_onesong/<int:id>",view=fetch_onesong,name="fetch_onesong"),
    path("fetch_oneuser/<int:id>",view=fetch_oneuser,name="fetch_oneuser"),
    path("edit_song/<int:id>",view=edit_song,name="edit_song"),
    path("edit_user/<int:id>",view=edit_user,name="edit_user"),
    path("delete_user/<int:id>",view=delete_user,name="delete_user"),
    path("delete_onesong/<int:id>",view=delete_onesong,name="delete_onesong"),
    path("create_record/<int:id>",view=create_record,name="create_record"),
    path("sign_in/",view=sign_in,name="sign_in"),
    path("sign_up/",view=sign_up,name="sign_up")


]



