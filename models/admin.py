from django.contrib import admin


from .models import AppAuthData,NotificationType,SubscriptionType,\
					UserNotificationType,catch_email_temp,organiser,team,player,\
					tournament,tournament_team_relationship,match,UserInfo,UserLog

admin.site.register(AppAuthData)
admin.site.register(NotificationType)
admin.site.register(SubscriptionType)
admin.site.register(UserNotificationType)
admin.site.register(catch_email_temp)
admin.site.register(organiser)
admin.site.register(team)
admin.site.register(player)
admin.site.register(tournament)
admin.site.register(tournament_team_relationship)
admin.site.register(match)
admin.site.register(UserInfo)
admin.site.register(UserLog)
