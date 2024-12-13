from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

import models
import schemas
from database import get_db

router = APIRouter(prefix="/zip_codes", tags=["ZipCodes"])


@router.get("/", response_model=List[schemas.ZipCodeAll])
def fetch_all(db: Session = Depends(get_db)):

    post = db.query(models.ZipCode).all()

    return post


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=List[schemas.CreateZipCode])
def post(post_post: schemas.CreateZipCode, db: Session = Depends(get_db)):

    new_post = models.ZipCode(**post_post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return [new_post]


@router.get("/{zip_code}", response_model=schemas.ZipCodeSingle, status_code=status.HTTP_200_OK)
def fetch_one(zip_code: str, db: Session = Depends(get_db)):

    idv_get = db.query(models.ZipCode).filter(models.ZipCode.zip_code == zip_code).first()

    if idv_get is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"The zip_code: {zip_code} you requested for does not exist"
        )
    return idv_get


@router.delete("/{zip_code}", status_code=status.HTTP_204_NO_CONTENT)
def delete(zip_code: str, db: Session = Depends(get_db)):

    deleted_post = db.query(models.ZipCode).filter(models.ZipCode.zip_code == zip_code)

    if deleted_post.first() is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"The zip_code: {zip_code} you requested for does not exist"
        )
    deleted_post.delete(synchronize_session=False)
    db.commit()


@router.put("/{zip_code}", response_model=schemas.ZipCodeSingle)
def update(update_post: schemas.ZipCodeSingle, zip_code: str, db: Session = Depends(get_db)):

    updated_post = db.query(models.ZipCode).filter(models.ZipCode.zip_code == zip_code)

    if updated_post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The zip_code:{zip_code} does not exist")
    updated_post.update(update_post.dict(), synchronize_session=False)
    db.commit()

    # return  updated_post.first()
