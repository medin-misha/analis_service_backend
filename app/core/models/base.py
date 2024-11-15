from sqlalchemy.orm import DeclarativeBase, declared_attr, mapped_column, Mapped


class Base(DeclarativeBase):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    @declared_attr.directive
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"
