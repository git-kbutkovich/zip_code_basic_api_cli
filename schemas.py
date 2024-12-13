from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel


class ZipCodeAll(BaseModel):
    zip_code: str
    city: str
    admin_region_code: str

    class Config:
        from_attributes = True


class ZipCodeSingle(BaseModel):
    country_code: str
    zip_code: str
    city: str
    admin_region_code: str
    latitude: Decimal
    longitude: Decimal
    # created_at: datetime
    # updated_at: datetime

    class Config:
        from_attributes = True
        # arbitrary_types_allowed=True


class CreateZipCode(ZipCodeSingle):
    class Config:
        from_attributes = True
