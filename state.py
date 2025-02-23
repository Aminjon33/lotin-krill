from aiogram.fsm.state import State, StatesGroup

class Registor(StatesGroup):
    name = State()
    surename = State()
    location = State()
    phone = State()

class Shop(StatesGroup):
    name = State()
    
class computers(StatesGroup):
    name = State()
    photo = State()
    price = State()
    color = State()

class Addcomputer(StatesGroup):
    LaptopAdd = State()
    LaptopUpdate = State()
    DeleteLaptop = State()

class SendReklama(StatesGroup):
    Adverts = State()