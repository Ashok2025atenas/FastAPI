from pydantic import BaseModel, EmailStr, ConfigDict


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    email: EmailStr | None = None
    password: str | None = None


class UserOut(BaseModel):
    id: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)
