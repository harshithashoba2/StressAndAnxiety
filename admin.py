from django.contrib import admin
from .models import Past_Appoint,Stageone,Stress_Stag2_ans,Anxiety_Stag2_ans,Outcome, Stage0,Appoint,common,Anxiety,Stress,People,Counselor,Doctor,Anxiety_Stag2,Stress_Stag2,RoomMember,Result,Profile
admin.site.register(common)
admin.site.register(Anxiety)
admin.site.register(Stress)
admin.site.register(People)
admin.site.register(Anxiety_Stag2)
admin.site.register(Stress_Stag2)
admin.site.register(Profile)
admin.site.register(Counselor)
admin.site.register(Doctor)
admin.site.register(Stage0)
admin.site.register(Outcome)
admin.site.register(RoomMember)
admin.site.register(Result)
admin.site.register(Appoint)
admin.site.register(Stress_Stag2_ans)
admin.site.register(Anxiety_Stag2_ans)
admin.site.register(Past_Appoint)

admin.site.register(Stageone)


