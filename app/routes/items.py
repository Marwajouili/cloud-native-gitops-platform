from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Item
from app.schemas import ItemCreate, ItemResponse

router = APIRouter(
    prefix="/api/items",
    tags=["items"],
)


@router.get("", response_model=list[ItemResponse])
def get_items(db: Session = Depends(get_db)):
    return db.query(Item).all()


@router.post("", response_model=ItemResponse)
def create_item(
    item_data: ItemCreate,
    db: Session = Depends(get_db),
):
    item = Item(
        name=item_data.name,
        description=item_data.description,
    )

    db.add(item)
    db.commit()
    db.refresh(item)

    return item