# urls.py
from django.urls import path
from . views import MarketDataList, \
                    Top5AirportsPaxByOrigin, \
                    Top5AirportsPaxByDestination, \
                    TopDistanceByMonth, \
                    Top5AirportsfreByOrigin, \
                    Top5AirportsfreByDestination, \
                    Top5AirportsMailByOrigin, \
                    Top5AirportsMailByDestination, \
                    Top5AirportsDisByOrigin, \
                    Top5AirportsDisByDestination, \
                    TopPassengersByMonth            


urlpatterns = [
    path('list/', MarketDataList.as_view(), name="list"),
    path('top5paxorigin/', 
        Top5AirportsPaxByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Passengers by Origin Airport"}
        ),
        name="top5paxorigin"),
    path('top5paxdestination/',  
        Top5AirportsPaxByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Passengers by Destination Airport"}
        ), 
        name="top5paxdestination"),
    path('topdistance_month/',  
        TopDistanceByMonth.as_view(
            extra_context={'title': "Top Distance by Month"}
        ), 
        name="topdistance_month"),
    path('top5freorigin/', 
        Top5AirportsfreByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - freight by Origin Airport"}
        ),
        name="top5freorigin"),
    path('top5fredestination/', 
        Top5AirportsfreByDestination.as_view(
            extra_context={'title': "Top 5 Airports - freight by Destination Airport"}
        ),
        name="top5fredestination"),
    path('top5mailorigin/', 
        Top5AirportsMailByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Mail by Origin Airport"}
        ),
        name="top5mailorigin"),
    path('top5maildestination/', 
        Top5AirportsMailByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Mail by Destination Airport"}
        ),
        name="top5maildestination"), 
    path('top5disorigin/', 
        Top5AirportsDisByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Distance by Origin Airport"}
        ),
        name="top5disorigin"),
    path('top5disdestination/', 
        Top5AirportsDisByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Distance by Destination Airport"}
        ),
        name="top5disdestination"),
    path('toppassengers_month/',  
        TopPassengersByMonth.as_view(
            extra_context={'title': "Most Passengers by Month"}
        ), 
        name="toppassengers_month"),               

]