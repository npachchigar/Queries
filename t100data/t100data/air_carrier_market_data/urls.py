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
                    TopPassengersByMonth, \
                    TopFreightCarriedAirline, \
                    TopPassengersCarriedAirline, \
                    TopMailCarriedAirline, \
                    LongDistanceAirline, \
                    AvgNumPassengersForLAX, \
                    AvgNumPassengersForSFO, \
                    AvgNumPassengersForDFW, \
                    AvgNumPassengersForATL, \
                    AvgNumPassengersForORD, \
                    TopPassengersByMonthForAA, \
                    AvgVolFreightForMIA, \
                    AvgVolFreightForMEM, \
                    AvgVolFreightForJFK, \
                    AvgVolFreightForANC, \
                    AvgVolFreightForSDF, \
                    CityFreightForLongDistance, \
                    CityMailForShortDistance, \
                    TopPassengersByMonthForAS, \
                    TopPassengersByMonthForDL, \
                    TopPassengersByMonthForUA, \
                    TopPassengersByMonthForWN                                                                      
                    

                                      


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
    path('topfreightcarriedairline/', 
        TopFreightCarriedAirline.as_view(
            extra_context={'title': "Most Freight Carried Airline"}
        ),
        name="topfreightcarriedairline"),
    path('toppassengerscarriedairline/', 
        TopPassengersCarriedAirline.as_view(
            extra_context={'title': "Most Passengers Carried Airline"}
        ),
        name="toppassengerscarriedairline"),
    path('topmailcarriedairline/', 
        TopMailCarriedAirline.as_view(
            extra_context={'title': "Most mail Carried Airline"}
        ),
        name="topmailcarriedairline"),
    path('longdistanceairline/', 
        LongDistanceAirline.as_view(
            extra_context={'title': "Long Distance Airline"}
        ),
        name="longdistanceairline"),    
    path('avgpassengersforlax/', 
        AvgNumPassengersForLAX.as_view(
            extra_context={'title': "Average Passengers Carried Airline"}
        ),
        name="avgpassengersforlax"),
    path('avgpassengersforsfo/', 
        AvgNumPassengersForSFO.as_view(
            extra_context={'title': "Average Passengers Carried Airline"}
        ),
        name="avgpassengersforsfo"), 
    path('avgpassengersfordfw/', 
        AvgNumPassengersForDFW.as_view(
            extra_context={'title': "Average Passengers Carried Airline"}
        ),
        name="avgpassengersfordfw"),
    path('avgpassengersforatl/', 
        AvgNumPassengersForATL.as_view(
            extra_context={'title': "Average Passengers Carried Airline"}
        ),
        name="avgpassengersforatl"), 
    path('avgpassengersforord/', 
        AvgNumPassengersForORD.as_view(
            extra_context={'title': "Average Passengers Carried Airline"}
        ),
        name="avgpassengersforord"),
    path('toppassengers_monthforaa/', 
        TopPassengersByMonthForAA.as_view(
            extra_context={'title': "Passengers Carried by Month For AA"}
        ),
        name="toppassengers_monthforaa"),
    path('toppassengers_monthforas/', 
        TopPassengersByMonthForAS.as_view(
            extra_context={'title': "Passengers Carried by Month For AS"}
        ),
        name="toppassengers_monthforas"),
    path('toppassengers_monthfordl/', 
        TopPassengersByMonthForDL.as_view(
            extra_context={'title': "Passengers Carried by Month For DL"}
        ),
        name="toppassengers_monthfordl"),
    path('toppassengers_monthforua/', 
        TopPassengersByMonthForUA.as_view(
            extra_context={'title': "Passengers Carried by Month For UA"}
        ),
        name="toppassengers_monthforua"), 
    path('toppassengers_monthforwn/', 
        TopPassengersByMonthForWN.as_view(
            extra_context={'title': "Passengers Carried by Month For WN"}
        ),
        name="toppassengers_monthforwn"),                
    path('avgfreightformia/', 
        AvgVolFreightForMIA.as_view(
            extra_context={'title': "Average Freight For MIA"}
        ),
        name="avgfreightformia"),
    path('avgfreightformem/', 
        AvgVolFreightForMEM.as_view(
            extra_context={'title': "Average Freight For MEM"}
        ),
        name="avgfreightformem"),  
    path('avgfreightforjfk/', 
        AvgVolFreightForJFK.as_view(
            extra_context={'title': "Average Freight For JFK"}
        ),
        name="avgfreightforjfk"),
    path('avgfreightforanc/', 
        AvgVolFreightForANC.as_view(
            extra_context={'title': "Average Freight For ANC"}
        ),
        name="avgfreightforanc"), 
    path('avgfreightforsdf/', 
        AvgVolFreightForSDF.as_view(
            extra_context={'title': "Average Freight For SDF"}
        ),
        name="avgfreightforsdf"),
    path('cityfreightlongdistance/', 
        CityFreightForLongDistance.as_view(
            extra_context={'title': "City Pairs Most Freight for long Distance"}
        ),
        name="cityfreightlongdistance"),
    path('citymailshortdistance/', 
        CityMailForShortDistance.as_view(
            extra_context={'title': "City Pairs Most Mail for Short Distance"}
        ),
        name="citymailshortdistance"),        

                                
]