from flet_route import path
from views import indexView, aboutAppView, aboutAppCity, museumInfoView, settings, allEventsViews, eventInfo, \
    supportView

app_routes = [
    path(url="/", clear=True, view=indexView),
    path(url="/mus/:id", clear=False, view=museumInfoView),
    path(url='/about_app/', clear=False, view=aboutAppView),
    path(url='/about_city/', clear=False, view=aboutAppCity),
    path(url='/settings/', clear=False, view=settings),
    path(url='/events/', clear=False, view=allEventsViews),
    path(url='/event/:id', clear=False, view=eventInfo),
    path(url='/support/', clear=False, view=supportView),
]

