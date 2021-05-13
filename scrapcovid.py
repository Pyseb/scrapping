import requests
from time import sleep

while True:
    r = requests.get("https://vitemadose.gitlab.io/vitemadose/70.json")
    centre_dispo=r.json().get("centres_disponibles", [])

    for centre in centre_dispo:
        url=centre.get('url')
        app_schedules=centre.get("appointment_schedules",[])
        for schedules in app_schedules:
            app_name=schedules.get('name','')
            if app_name != "chronodose":
                continue
            total_dose=schedules.get('total')
            if total_dose>0:
                print (url)
    print ('rien de nouveau')
    sleep (600)