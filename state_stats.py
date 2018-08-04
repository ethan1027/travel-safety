import pandas as pd
import os
import django
import numpy as np
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_safety.settings')
path = 'E:\Coding Repository\VisualCodeProjects\gun_stats_senior_project\gun-violence-data.csv'
path_pop = 'E:\Coding Repository\VisualCodeProjects\gun_stats_senior_project\pop.csv'
django.setup()
from stats_app.models import State
df_alldata = pd.read_csv(path)
state_incident_series = df_alldata['state'].value_counts() #get result
print(state_incident_series)
population_df = pd.read_csv(path_pop)
state_incident_pop = []

for index, row in population_df.iterrows():
    state_name = row['state']
    state_incident_100 = float(state_incident_series[state_name])*100000/float((row['population'].replace(',','')))
    state_incident_pop.append((state_name, state_incident_100))
state_incident_pop = np.array(state_incident_pop, dtype=[('state', object), ('inc', float)])
state_incident_pop = np.sort(state_incident_pop, order='inc')
state_incident_pop = state_incident_pop[::-1] #get result
state_incident_pop_series = pd.Series([state[1] for state in state_incident_pop], index=[state[0] for state in state_incident_pop])
print(state_incident_pop_series)

state_loss_df = df_alldata.groupby(['state'])[['n_killed','n_injured']].sum()
state_loss_df['n_loss'] = state_loss_df['n_injured']+state_loss_df['n_killed']
state_loss_df = state_loss_df.sort_values(by='n_loss', ascending=False)
state_loss_name_arr = np.array(state_loss_df.index.values)
state_loss_series = pd.Series(state_loss_df['n_loss'], index=state_loss_name_arr)
print(state_loss_series)

state_incident_arr = np.array(state_incident_series)
state_rank = []
for i, value in np.ndenumerate(state_incident_pop):
    state_name = value[0]
    rank_1 = i[0]
    rank_2 = np.argwhere(state_incident_arr==state_incident_series[state_name])
    rank_2 = rank_2[0]
    rank_3 = np.argwhere(state_loss_name_arr==state_name)
    rank_3 = rank_3[0]
    state_rank.append((state_name, rank_1 + rank_2[0]*2 + rank_3[0]*1.5))

state_rank = np.array(sorted(state_rank, key= lambda state: state[1]))
official_state_rank = []
counter = 1
rank = 1
last = 100
for state in state_rank:
    official_state_rank.append((state[0], rank))
    counter += 1
    if not state[1] == last:
        rank = counter
    last = state[1]

official_state_rank_series = pd.Series([state[1] for state in official_state_rank], index=[state[0] for state in official_state_rank])
print(official_state_rank_series)


state_list = []
i_delete = np.argwhere(state_loss_name_arr=='District of Columbia')
state_loss_name_arr = np.delete(state_loss_name_arr, i_delete)

print(state_loss_name_arr)
for state_name in state_loss_name_arr:
    state_model = State(name=state_name, rank=official_state_rank_series[state_name], 
total_incidents=state_incident_series[state_name], total_killed_n_injured=state_loss_series[state_name], 
incidents_per_100k=state_incident_pop_series[state_name])
    state_list.append(state_model)

State.objects.bulk_create(state_list)
print('done')