from typing import List

from fastapi import APIRouter, Depends, status, Query
from fastapi.responses import Response

from app.database.schemas.expenses_schemas import Expense, ExpenseCreate, ExpenseUpdate
from app.database.schemas.main_schemas import Period
from app.database.schemas.users_schemas import User
from app.services.auth_service import get_current_user
from app.services.expences_service import ExpenseService

router = APIRouter(
    prefix="/expenses",
    tags=["Расходы"]
)


@router.get("/", response_model=List[Expense])
async def get_expenses(
        period: Period = Depends(),
        user_id: int = Depends(get_current_user),
        service: ExpenseService = Depends()
):
    return service.get_expenses(user_id, period)


@router.post("/", response_model=Expense)
async def create_expense(
        expense: ExpenseCreate,
        user_id: int = Depends(get_current_user),
        service: ExpenseService = Depends()
):
    return service.create_expense(user_id, expense)


@router.put("/{expense_id}", response_model=Expense)
async def update_expense(
        expense_id: int,
        expense: ExpenseUpdate,
        user_id: int = Depends(get_current_user),
        service: ExpenseService = Depends()
):
    return service.update_expense(
        user_id=user_id,
        expense_id=expense_id,
        expense_data=expense
    )


@router.delete("/{expense_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_expense(
        expense_id: int,
        user_id: int = Depends(get_current_user),
        service: ExpenseService = Depends()
):
    service.delete_expense(user_id, expense_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
