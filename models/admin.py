from django.contrib import admin


from .models import organiser,team,player,tournament,tournament_team_relationship,match
admin.site.register(organiser)
admin.site.register(team)
admin.site.register(player)
admin.site.register(tournament)
admin.site.register(tournament_team_relationship)
admin.site.register(match)
