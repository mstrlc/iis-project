from transport.models import User, Stop, Line, Vehicle, Connection

import random

def generate_random_names(num_names, entity):
    first_names = ["Ethan", "Olivia", "Mason", "Zoe", "Lucas", "Ava", "Logan", "Isabella", "Jackson", "Chloe", "Noah", "Sophia", "Aiden", "Amelia", "Owen", "Harper", "Carter", "Grace", "Landon", "Mia"]
    last_names = ["Wheeler", "Brooks", "Porter", "Carrington", "Vaughn", "Donovan", "Harper", "Chandler", "Mercer", "Sinclair", "Garrison", "Prescott", "Drake", "Hayes", "Montgomery", "Kensington", "Whitman", "Winslow", "Ashton", "Kensington"]
    brno_prefixes = ["Morava", "Vele", "Špilberk", "Masaryk", "Zelný", "Brněnský", "Lužánecký", "Sono", "Husa", "Veveří"]
    brno_suffixes = ["Expres", "Navigátor", "Běžec", "Voyager", "Pionýr", "Křižník", "Hledač", "Kluzák", "Sprint", "Interceptor"]

    if entity == "user":
        prefixes = first_names
        suffixes = last_names
    elif entity == "vehicle":
        prefixes = brno_prefixes
        suffixes = brno_suffixes
    names = []
    for _ in range(num_names):
        first_name = random.choice(prefixes)
        last_name = random.choice(suffixes)
        names.append(f"{first_name} {last_name}")

    return names

def insert_sample_users():
    from transport.models import User
    users = [ "admin", "manager", "technician", "dispatcher", "driver", "customer" ]
    names = generate_random_names(len(users), "user")
    # for each check if users already exist
    for i, user in enumerate(users):
        if not User.query.filter_by(email=f'{user}@transport.com').first():
            new_user = User(email=f'{user}@transport.com', firstname=names[i].split(' ', 1)[0], lastname=names[i].split(' ', 1)[1], role=user)
            new_user.password = user
            new_user.save()

def insert_sample_vehicles():
    from transport.models import Vehicle
    vehicles = [ "bus", "tram", "trolleybus" ]
    make = [ "Iveco" , "Mercedes-Benz", "Solaris" ]
    model = [ "Urbanway", "Citaro", "Urbino" ]
    specs = [ "8-válec, automat., 180 km/h", "6-válec, automat., 160 km/h", "4-válec, automat., 140 km/h" ]
    status = [ "available", "unavailable", "maintenance" ]
    names = generate_random_names(len(vehicles), "vehicle")
    # for each check if users already exist
    for i, vehicle in enumerate(vehicles):
        if not Vehicle.query.filter_by(type=vehicle).first():
            new_vehicle = Vehicle(name=names[i], type=vehicle, make=make[i], model=model[i], specs=specs[i], status=status[i] )
            new_vehicle.save()
    
def insert_sample_stops():
    from transport.models import Stop
    stops = [ "Jugoslávská", "Semilasso", "Hlavní nádraží" ]
    longitudes = [ "49.2044942N", "49.2277139N", "49.1911869N" ] 
    latitudes = [ "16.6237300E", "16.5925569E", "16.6122861E" ]
    # for each check if users already exist
    for i, stop in enumerate(stops):
        if not Stop.query.filter_by(name=stop).first():
            new_stop = Stop(name=stop, latitude=latitudes[i], longitude=longitudes[i])
            new_stop.save()

def insert_sample_lines():
    from transport.models import Line
    lines = [ "1", "2", "3" ]
    # for each check if users already exist
    for line in lines:
        if not Line.query.filter_by(name=line).first():
            new_line = Line(name=line)
            new_line.save()
