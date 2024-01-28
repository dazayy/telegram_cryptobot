from aiogram.fsm.state import StatesGroup, State

# class состояний 

class RegisterState(StatesGroup):
    regname = State() # имя пользователя