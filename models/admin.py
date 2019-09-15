from django.contrib import admin


from .models import AppAuthData,NotificationType,SubscriptionType,\
					UserNotificationType,catch_email_temp,Organiser,Team,Player,\
					Tournament,TournamentTeamRelationship,Match,UserInfo,UserLog

admin.site.register(AppAuthData)
admin.site.register(NotificationType)
admin.site.register(SubscriptionType)
admin.site.register(UserNotificationType)
admin.site.register(catch_email_temp)
admin.site.register(Organiser)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Tournament)
admin.site.register(TournamentTeamRelationship)
admin.site.register(Match)
admin.site.register(UserInfo)
admin.site.register(UserLog)
