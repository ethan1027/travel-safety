import pandas as pd
import os 
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_safety.settings')
path = 'E:\Coding Repository\VisualCodeProjects\gun_stats_senior_project\gun-violence-data.csv'
django.setup()
from stats_app.models import State
df_alldata = pd.read_csv(path)
dfs['date'] = pd.to_datetime(dfs['date'])
print(dfs.dtypes)
gunshot_list = []
for index, df in dfs.iterrows():
    g = Gunshot(incident_id=df['incident_id'], state=df['state'], city_or_county=df['city_or_county'], 
    address=df['address'], lat=round(df['latitude'],4), lng=round(df['longitude'],4))
    gunshot_list.append(g)


Gunshot.objects.bulk_create(gunshot_list)
print('done')

""" g = Gunshot(incident_id=df['incident_id'], date=df['date'], state=df['state'], city_or_county=df['city_or_county'], address=df['address'], 
n_killed=df['n_killed'], n_injured=df['n_injured'], incident_url=df['incident_url'], source_url=df['source_url'], 
incident_url_fields_missing=df['incident_url_fields_missing'], congressional_district=df['congressional_district'], 
gun_stolen=df['gun_stolen'], gun_type = df['gun_type'], incident_characteristics=df['incident_characteristics'], lat=df['latitude'], 
location_description=df['location_description'], lng=df['longitude'], n_guns_involved=df['n_guns_involved'], notes=df['notes'], 
participant_age=df['participant_age'], participant_age_group=df['participant_age_group'], participant_gender=df['participant_gender'], 
participant_name=df['participant_name'], participant_relationship=df['participant_relationship'], participant_status=df['participant_status'],
participant_type=df['participant_type'], sources=df['sources'], state_house_district=df['state_house_district'], state_senate_district=df['state_senate_district'],) """


