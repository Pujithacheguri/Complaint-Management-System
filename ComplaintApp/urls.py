from django.urls import path

from . import views

urlpatterns = [path("index.html", views.index, name="index"),
               path("AdminLogin.html", views.AdminLogin, name="AdminLogin"),	      
               path("AdminLoginAction", views.AdminLoginAction, name="AdminLoginAction"),
               path("UserLoginAction", views.UserLoginAction, name="UserLoginAction"),
               path("UserLogin.html", views.UserLogin, name="UserLogin"),
               path("ViewComplaints", views.ViewComplaints, name="ViewComplaints"),
	       path("OTPAction", views.OTPAction, name="OTPAction"),	    
	       path("TextComplaintAction", views.TextComplaintAction, name="TextComplaintAction"),
               path("TextComplaint.html", views.TextComplaint, name="TextComplaint"),
	       path("UploadAudioAction", views.UploadAudioAction, name="UploadAudioAction"),
               path("UploadAudio.html", views.UploadAudio, name="UploadAudio"),
	       path("TrackComplaint", views.TrackComplaint, name="TrackComplaint"),
	       path("DeleteComplaint", views.DeleteComplaint, name="DeleteComplaint"),
	       path("ViewComplaints", views.ViewComplaints, name="ViewComplaints"),
	       path("UpdateStatus", views.UpdateStatus, name="UpdateStatus"),
]
