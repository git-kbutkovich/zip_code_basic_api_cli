from sqlalchemy import Column
from sqlalchemy.types import DECIMAL, TEXT, TIMESTAMP, String

from database import Base


class ZipCode(Base):
    __tablename__ = "zip_codes"

    country_code = Column(String, nullable=False)
    zip_code = Column(String, nullable=False, primary_key=True)
    city = Column(String, nullable=True)
    admin_region = Column(String, nullable=True)
    admin_region_code = Column(String, nullable=True)
    admin_subregion = Column(String, nullable=True)
    admin_subregion_code = Column(String, nullable=True)
    admin_subregion_code_2 = Column(String, nullable=True)
    admin_subregion_code_2 = Column(String, nullable=True)
    latitude = Column(DECIMAL, nullable=False)
    longitude = Column(DECIMAL, nullable=False)
    # created_at = Column(TIMESTAMP(timezone=False))  # , server_default=String('now()'))
    # updated_at = Column(TIMESTAMP(timezone=False))  # , server_default=TEXT('now()'))

