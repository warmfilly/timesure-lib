class CategoryManager:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.engine = self.get_engine()

    
    def get_engine(self):
        return create_engine('sqlite:///' + self.db_path)


    def get_all(self) -> List[Category]:
        stmt = select(Category)
        
        with Session(self.engine) as session:
            for row in session.scalars(stmt):
                yield row