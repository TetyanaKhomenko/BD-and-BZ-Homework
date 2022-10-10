from http.client import PROXY_AUTHENTICATION_REQUIRED


class Clients:
    def __init__(self, client_id, name, surname, gender):
        self.client_id = client_id
        self.name =name
        self.surname = surname
        self.gender = gender

class Available_services:
    def __init__(self, avser_id, service_name, time):
        self.avser_id = avser_id
        self.service_name = service_name
        self.time = time
        
class Masters:
    def __init__(self, master_id, master_name, level):
        self.master_id = master_id
        self.master_name = master_name
        self.level = level


class Price:
    def __init__(self, price_id):
        self.price_id = price_id



        
