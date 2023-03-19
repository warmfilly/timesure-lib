from sqlalchemy import create_engine     
#from .managers import CategoryManager, ActivityManager 


class TimesureStore:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.engine = create_engine('sqlite:///' + db_path)

