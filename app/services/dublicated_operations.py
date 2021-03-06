from fastapi import HTTPException, status
from pydantic import BaseModel
from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.database.database import Base
from app.database.models import tables
from app.database.schemas.main_schemas import Period
from app.utils import validator


def get_user(session: Session, user_id: int) -> tables.User:
    user = session.query(tables.User).get(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Пользователя с идентификатором {user_id} нет в базе!"
        )
    return user


def check_user(session: Session, user_id: int) -> tables.User:
    user = get_user(session, user_id)
    if user.company_id is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Вы не состоите в компании!"
        )

    return user


def check_permission(session: Session, user_id: int) -> tables.User:
    user = check_user(session, user_id)
    if not user.chief:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="У вас нет прав на это действие!"
        )

    return user


def get(
        session: Session,
        table: Base,
        user_id: int,
        period: Period
):
    user = check_user(session, user_id)
    data = (
        session
            .query(table)
            .filter_by(company_id=user.company_id)
            .where(table.date >= period.from_date)
            .where(table.date < period.to_date)
            .order_by(desc(table.date))
            .all()
    )
    return data


def update(
        session: Session,
        table: Base,
        user_id: int,
        item_id: int,
        item_data: BaseModel
):
    item = (
        session
            .query(table)
            .filter_by(id=item_id)
            .first()
    )
    validator.is_none_check(item)
    for field, value in item_data:
        setattr(item, field, value)
    item.user_id = user_id
    session.commit()
    session.refresh(item)
    return item


def delete(
        session: Session,
        item_id: int,
        table: Base
) -> None:
    item = (
        session
            .query(table)
            .filter_by(id=item_id)
            .first()
    )
    validator.is_none_check(item)
    session.delete(item)
    session.commit()
