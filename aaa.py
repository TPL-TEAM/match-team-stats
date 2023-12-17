import json
import requests

list1d = []
ids = []
with open('dzien.json', 'r+') as file:
    dane = json.loads(file.read())
    for events in dane["Stages"]:
        for teams in events["Events"]:
            try:
                list1d.append(events['CompId'])
            except:
                list1d.append('12')
            for team1 in teams['T1']:
                list1d.append(team1['ID'])

            for team2 in teams['T2']:
                list1d.append(team2['ID'])

            ids.append(list1d)
            list1d = []






    # for events in dane["Stages"]:
    #     for teams in events["Events"]:
    #         if(events['CompId'] == '65' or events['CompId'] == '67' or events['CompId'] == '75' or events['CompId'] == '68' or events['CompId'] == '77'):
    #             with open('liga.json', 'r+') as file:
    #                 tab = json.loads(file.read())
    #                 for i in range(0, 30):
    #                     id1 = tab["LeagueTable"]["L"][0]["Tables"][0]["team"][i]['Tid']
    #                     for team1 in teams['T1']:
    #                         if(id1==team1['ID']):
    #                             break
                                
    #                 for i in range(0, 30):
    #                     id2 = tab["LeagueTable"]["L"][0]["Tables"][0]["team"][i]['Tid']
    #                     print(id2)
    #                     for team2 in teams['T2']:
    #                         if(id2==team2['ID']):
    #                             break
    
    #                 if(abs(id1-id2)>=5):
    #                     list1d.append(events['CompId'])
                            
    #                     list1d.append(team1['ID'])
    #                     list1d.append(id1)

    #                     list1d.append(team2['ID'])
    #                     list1d.append(id2)
            

    #         ids.append(list1d)
    #         list1d = []

print(ids)