from pydantic import BaseModel, Field, field_validator


class Wine(BaseModel):
    id: int
    points: int
    title: str
    description: str | None
    price: float | None
    variety: str | None
    winery: str | None
    country: str | None
    province: str | None
    region_1: str | None
    region_2: str | None
    vineyard: str | None = Field(alias="designation")
    taster_name: str | None
    taster_twitter_handle: str | None

    @field_validator("country")
    def validate_country(cls, value: str | None) -> str:
        if value is None:
            return "Unknown"
        return value