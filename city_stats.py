import pandas as pd
import os
import django
import numpy as np
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_safety.settings')
path = 'E:\Coding Repository\VisualCodeProjects\gun_stats_senior_project\gun-violence-data.csv'
path_pop = 'E:\Coding Repository\VisualCodeProjects\gun_stats_senior_project\pop.csv'
django.setup()
from stats_app.models import City
df_alldata = pd.read_csv(path)
df_alldata['city'] = df_alldata['city_or_county'].map(str) + ', ' + df_alldata['state']
city_incident_series = df_alldata['city'].value_counts()
print(len(city_incident_series))
city_name_incident_arr = city_incident_series.index.values
print(city_name_incident_arr)
city_rank_series = pd.Series(list(range(1,len(city_name_incident_arr)+1)), index=city_name_incident_arr)
print(city_rank_series)

city_list = []
for city_name in city_name_incident_arr:
    city_model = City(name=city_name, rank=city_rank_series[city_name], total_incidents=city_incident_series[city_name])
    city_list.append(city_model)

City.objects.bulk_create(city_list)
print('done')
