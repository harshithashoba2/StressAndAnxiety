from django.urls import path
from . import views
 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns =[
    path("",views.home,name="home"),
    path("register",views.register,name="register"),
    path("login",views.begin,name="begin"),
    path("out",views.out,name="out"),
    path("stage1",views.stage1,name="stage1"),
    path("contact",views.contact,name="contact"),
    path("Anxiety_Stag2",views.anxiety_Stag2,name="Anxiety_Stag2"),
    path("Stress_Stag2",views.stress_Stag2,name="Stress_Stag2"),
    path("stage3",views.stage3,name="stage3"),
    path("stage0",views.stage0,name="stage0"),
    path("panic",views.panic,name="panic"),
    path("gad/",views.gad,name="gad"),
    path("lobby/",views.lobby,name="lobby"),
    path("chatroom/",views.chatroom,name="chatroom"),
    path("getToken/",views.getToken,name="getToken"),
    path("create_member/",views.createMember,name="createUser"),
    path("get_member/",views.getMember,name="getUser"),
    path("delete_member/",views.deleteMember,name="deleteUser"),
    path("stage3_p/",views.panic,name="panic"),
    path("stage3_g/",views.gad,name="gad"),
    path("stage3_s",views.social,name="social"),
    path("stage3_pt/",views.ptsd,name="ptsd"),
    path("stage3_a",views.acute,name="acute"),
    path("stage3_adjust",views.adjust,name="adjust"),
    path("counsellor/",views.counsellor,name="counsellor"),
    path("doctor/",views.doctor,name="doctor"),
    path("counsellor_profile/",views.counsellor_profile,name="counsellor_profile"),
    path("doctor_profile/",views.doctor_profile,name="doctor_profile"),
    path("low/",views.low,name="low"),
    path("high/",views.high,name="high"),
    path("user_lobby/",views.user_lobby,name="user_lobby"),
    path("document/<int:obj>",views.document,name="document"),
    path("invite/",views.invite,name="invite"),
    path("activate/<uid64>/<token>",views.activate,name="activate"),
    path("personal/",views.personal,name="personal"),
    path("response/",views.response,name="response"),
    path("get_lat_long/<int:obj>",views.get_lat_long,name="get_lat_long"),
    path("doctors/",views.doctors,name="doctors"),
    path("find_nearby_doctors/<int:prof>/<int:doc>/",views.find_nearby_doctors,name="find_nearby_doctors"),
    path("appoint/<int:obj>",views.appoint,name="appoint"),
    path("docum_doc/<int:obj>",views.docum_doc,name="docum_doc"),
    path("addcolumn/<int:obj>",views.addcolumn,name="addcolumn"),
    path("coun_app",views.coun_app,name="coun_app"),
    path("terms",views.terms,name="terms"),
    path('password_reset/',views.password_reset_view,name='password_reset_view'),
    path("resone/",views.resone,name="resone"),
    path("navi",views.navi,name="navi"),
    path("logout_h",views.logout_h,name="logout_h"),
    path("logout_s",views.logout_s,name="logout_s"),
    
    path('password_reset_confirm/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    
    
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
