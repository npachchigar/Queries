# Create your views here.
from functools import update_wrapper
import pdb
from django.db.models.aggregates import Avg
from django.views.generic import ListView
from django.db.models import Max, Sum, Min

from . models import MarketData

class MarketDataList(ListView):
    model = MarketData

# What are the top 5 airports in terms of: Total passengers by origin
class Top5AirportsPaxByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_pax=Sum('passengers')) \
                        .order_by('-total_pax')[0:5]
    template_name="rankorder_list_origin.html"

# What are the top 5 airports in terms of: Total passengers by destination
class Top5AirportsPaxByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_pax=Sum('passengers')) \
                                 .order_by('-total_pax')[0:5]
    template_name="rankorder_list_destination.html"


# Which airport reported the longest distance by month?
class TopDistanceByMonth(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_distance_month.html"

    def get_queryset(self):

        month_list = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name',
                        'month') \
                .filter(month__exact=month) \
                .annotate(total_distance=Max('distance')) \
                .order_by('-total_distance')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list


# What are the top 5 airports in terms of: Total freight by origin
class Top5AirportsfreByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_fre=Sum('freight')) \
                        .order_by('-total_fre')[0:5]
    template_name="rankorder_list_origin_freight.html"

# What are the top 5 airports in terms of: Total freight by destination
class Top5AirportsfreByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('dest_iata_code','dest_city_name') \
                        .annotate(total_fre=Sum('freight')) \
                        .order_by('-total_fre')[0:5]
    template_name="rankorder_list_destination_freight.html"


# What are the top 5 airports in terms of: Total mail by origin
class Top5AirportsMailByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_mail=Sum('mail')) \
                        .order_by('-total_mail')[0:5]
    template_name="rankorder_list_origin_mail.html"

# What are the top 5 airports in terms of: Total mail by destination
class Top5AirportsMailByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('dest_iata_code','dest_city_name') \
                        .annotate(total_mail=Sum('mail')) \
                        .order_by('-total_mail')[0:5]
    template_name="rankorder_list_destination_mail.html"


# What are the top 5 airports in terms of: Total distance by origin
class Top5AirportsDisByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_dis=Sum('distance')) \
                        .order_by('-total_dis')[0:5]
    template_name="rankorder_list_origin_distance.html"

# What are the top 5 airports in terms of: Total distance by destination
class Top5AirportsDisByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('dest_iata_code','dest_city_name') \
                        .annotate(total_dis=Sum('distance')) \
                        .order_by('-total_dis')[0:5]
    template_name="rankorder_list_destination_distance.html"


# Which airport reported the most passengers by month?
class TopPassengersByMonth(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_passengers_month.html"

    def get_queryset(self):

        month_list = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name',
                        'month') \
                .filter(month__exact=month) \
                .annotate(total_passengers=Max('passengers')) \
                .order_by('-total_passengers')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list


# Which airline reported the most freight carried?
class TopFreightCarriedAirline(ListView):
    context_object_name = "airline_list"
    queryset = MarketData.objects \
                        .values('carrier_id','carrier_name') \
                        .annotate(total_fre=Sum('freight')) \
                        .order_by('-total_fre')[0:1]                                     
    template_name="most_freight_carried_airline.html"   


# Which airline reported the most passengers carried?
class TopPassengersCarriedAirline(ListView):
    context_object_name = "airline_list"
    queryset = MarketData.objects \
                        .values('carrier_id','carrier_name') \
                        .annotate(total_pax=Sum('passengers')) \
                        .order_by('-total_pax')[0:1]                   
    template_name="most_passengers_carried_airline.html" 


# Which airline reported the most mail carried?
class TopMailCarriedAirline(ListView):
    context_object_name = "airline_list"
    queryset = MarketData.objects \
                        .values('carrier_id','carrier_name') \
                        .annotate(total_mail=Sum('mail')) \
                        .order_by('-total_mail')[0:1]                   
    template_name="most_mail_carried_airline.html" 


# Which airline reported the longest flight distance?
class LongDistanceAirline(ListView):
    context_object_name = "airline_list"
    queryset = MarketData.objects \
                        .values('carrier_id','carrier_name') \
                        .annotate(total_distance=Sum('distance')) \
                        .order_by('-total_distance')[0:1]                   
    template_name="long_distance_airline.html"                                     
     
# Find the average number of passengers for flights into:
# LAX (Los Angeles)
class AvgNumPassengersForLAX(ListView):
    context_object_name = "airline_list"
    queryset = MarketData.objects \
                        .values('dest_city_name', 'dest_iata_code') \
                        .annotate(total_pax=Avg('passengers')) \
                        .filter(dest_iata_code='LAX')                   
    template_name="avg_passengers.html" 

# SFO (San Francisco)
class AvgNumPassengersForSFO(ListView):
    context_object_name = "airline_list"
    queryset = MarketData.objects \
                        .values('dest_city_name', 'dest_iata_code') \
                        .annotate(total_pax=Avg('passengers')) \
                        .filter(dest_iata_code='SFO')                   
    template_name="avg_passengers.html"

# DFW (Dallas-Fort Worth)
class AvgNumPassengersForDFW(ListView):
    context_object_name = "airline_list"
    queryset = MarketData.objects \
                        .values('dest_city_name', 'dest_iata_code') \
                        .annotate(total_pax=Avg('passengers')) \
                        .filter(dest_iata_code='DFW')                   
    template_name="avg_passengers.html"

# ATL (Atlanta)
class AvgNumPassengersForATL(ListView):
    context_object_name = "airline_list"
    queryset = MarketData.objects \
                        .values('dest_city_name', 'dest_iata_code') \
                        .annotate(total_pax=Avg('passengers')) \
                        .filter(dest_iata_code='ATL')                   
    template_name="avg_passengers.html" 

# ORD (Chicago)
class AvgNumPassengersForORD(ListView):
    context_object_name = "airline_list"
    queryset = MarketData.objects \
                        .values('dest_city_name', 'dest_iata_code') \
                        .annotate(total_pax=Avg('passengers')) \
                        .filter(dest_iata_code='ORD')                   
    template_name="avg_passengers.html" 


# Rank order passengers carried, by month, for these airlines
# AA (American Airlines)                   
class TopPassengersByMonthForAA(ListView):
    context_object_name = "airline_list"
    template_name="rankorder_passengers_month_for_airline.html"

    def get_queryset(self):

        month_list = []

        for month in range(1,7):
            queryset = MarketData.objects \
                .values('carrier_id',
                        'carrier_name',
                        'month') \
                .filter(month__exact=month, carrier_id='AA') \
                .annotate(total_pax=Sum('passengers')) \
                .order_by('-total_pax')            
                
            # off by one error for assignment

            month_list.append(queryset)
        
        def get_passengers(filtered_data_list_elem):
            return filtered_data_list_elem[0].get('total_pax')

        month_list.sort(key=get_passengers, reverse=True)
        # return list
        return month_list

# AS (Alaska Airlines)
class TopPassengersByMonthForAS(ListView):
    context_object_name = "airline_list"
    template_name="rankorder_passengers_month_for_airline.html"

    def get_queryset(self):

        month_list = []

        for month in range(1,7):
            queryset = MarketData.objects \
                .values('carrier_id',
                        'carrier_name',
                        'month') \
                .filter(month__exact=month, carrier_id='AS') \
                .annotate(total_pax=Sum('passengers')) \
                .order_by('-total_pax')            
                
            # off by one error for assignment

            month_list.append(queryset)
        
        def get_passengers(filtered_data_list_elem):
            return filtered_data_list_elem[0].get('total_pax')

        month_list.sort(key=get_passengers, reverse=True)
        # return list
        return month_list

# DL (Delta Airlines)
class TopPassengersByMonthForDL(ListView):
    context_object_name = "airline_list"
    template_name="rankorder_passengers_month_for_airline.html"

    def get_queryset(self):

        month_list = []

        for month in range(1,7):
            queryset = MarketData.objects \
                .values('carrier_id',
                        'carrier_name',
                        'month') \
                .filter(month__exact=month, carrier_id='DL') \
                .annotate(total_pax=Sum('passengers')) \
                .order_by('-total_pax')            
                
            # off by one error for assignment

            month_list.append(queryset)
        
        def get_passengers(filtered_data_list_elem):
            return filtered_data_list_elem[0].get('total_pax')

        month_list.sort(key=get_passengers, reverse=True)
        # return list
        return month_list

# UA (United Airlines)
class TopPassengersByMonthForUA(ListView):
    context_object_name = "airline_list"
    template_name="rankorder_passengers_month_for_airline.html"

    def get_queryset(self):

        month_list = []

        for month in range(1,7):
            queryset = MarketData.objects \
                .values('carrier_id',
                        'carrier_name',
                        'month') \
                .filter(month__exact=month, carrier_id='UA') \
                .annotate(total_pax=Sum('passengers')) \
                .order_by('-total_pax')            
                
            # off by one error for assignment

            month_list.append(queryset)
        
        def get_passengers(filtered_data_list_elem):
            return filtered_data_list_elem[0].get('total_pax')

        month_list.sort(key=get_passengers, reverse=True)
        # return list
        return month_list

# WN (Southwest Airlines)
class TopPassengersByMonthForWN(ListView):
    context_object_name = "airline_list"
    template_name="rankorder_passengers_month_for_airline.html"

    def get_queryset(self):

        month_list = []

        for month in range(1,7):
            queryset = MarketData.objects \
                .values('carrier_id',
                        'carrier_name',
                        'month') \
                .filter(month__exact=month, carrier_id='WN') \
                .annotate(total_pax=Sum('passengers')) \
                .order_by('-total_pax')            
                
            # off by one error for assignment

            month_list.append(queryset)
        
        def get_passengers(filtered_data_list_elem):
            return filtered_data_list_elem[0].get('total_pax')

        month_list.sort(key=get_passengers, reverse=True)
        # return list
        return month_list        

# Find the average volume of freight for flights departing
# MIA (Miami)
class AvgVolFreightForMIA(ListView):
    context_object_name = "airline_list"
    queryset = MarketData.objects \
                        .values('orig_city_name', 'orig_iata_code') \
                        .annotate(total_fre=Avg('freight')) \
                        .filter(orig_iata_code='MIA')                   
    template_name="avg_freight.html" 

# MEM (Memphis)
class AvgVolFreightForMEM(ListView):
    context_object_name = "airline_list"
    queryset = MarketData.objects \
                        .values('orig_city_name', 'orig_iata_code') \
                        .annotate(total_fre=Avg('freight')) \
                        .filter(orig_iata_code='MEM')                   
    template_name="avg_freight.html"

# JFK (New York JFK)
class AvgVolFreightForJFK(ListView):
    context_object_name = "airline_list"
    queryset = MarketData.objects \
                        .values('orig_city_name', 'orig_iata_code') \
                        .annotate(total_fre=Avg('freight')) \
                        .filter(orig_iata_code='JFK')                   
    template_name="avg_freight.html"

# ANC (Anchorage)
class AvgVolFreightForANC(ListView):
    context_object_name = "airline_list"
    queryset = MarketData.objects \
                        .values('orig_city_name', 'orig_iata_code') \
                        .annotate(total_fre=Avg('freight')) \
                        .filter(orig_iata_code='ANC')                   
    template_name="avg_freight.html"        


# SDF (Louisville)
class AvgVolFreightForSDF(ListView):
    context_object_name = "airline_list"
    queryset = MarketData.objects \
                        .values('orig_city_name', 'orig_iata_code') \
                        .annotate(total_fre=Avg('freight')) \
                        .filter(orig_iata_code='SDF')                   
    template_name="avg_freight.html"


# What city pairs represent the most freight carried for the longest distance?
class CityFreightForLongDistance(ListView):
    context_object_name = "city_list"
    queryset = MarketData.objects \
                        .values('orig_city_name','dest_city_name','freight') \
                        .annotate(total_distance=Max('distance'), total_freight=Max('freight')) \
                        .order_by('-total_distance')[0:1]                                          
    template_name="city_freight_long_distance.html"


# What city pairs represent the most mail carried for the shortest distance?    
class CityMailForShortDistance(ListView):
    context_object_name = "city_list"
    queryset = MarketData.objects \
                        .values('orig_city_name','dest_city_name', 'mail') \
                        .annotate(total_mail=Sum('mail'), total_distance=Min('distance')) \
                        .order_by('-total_distance').reverse()[0:1]
                      
    template_name="city_mail_short_distance.html"                    
                                      
    
