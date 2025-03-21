from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import engine, get_db

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.post("/restaurants/", response_model=schemas.RestaurantResponse)
def create_restaurant(restaurant: schemas.RestaurantCreate, db: Session = Depends(get_db)):
    db_restaurant = models.Restaurant(**restaurant.model_dump())
    db.add(db_restaurant)
    db.commit()
    db.refresh(db_restaurant)
    return db_restaurant

@app.get("/restaurants/", response_model=list[schemas.RestaurantResponse])
def get_restaurants(db: Session = Depends(get_db)):
    return db.query(models.Restaurant).all()

@app.get("/restaurants/{restaurant_id}", response_model=schemas.RestaurantResponse)
def get_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    restaurant = db.query(models.Restaurant).filter(models.Restaurant.id == restaurant_id).first()
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return restaurant

@app.put("/restaurants/{restaurant_id}", response_model=schemas.RestaurantResponse)
def update_restaurant(restaurant_id: int, updated_data: schemas.RestaurantCreate, db: Session = Depends(get_db)):
    restaurant = db.query(models.Restaurant).filter(models.Restaurant.id == restaurant_id).first()
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")

    for key, value in updated_data.model_dump().items():
        setattr(restaurant, key, value)

    db.commit()
    db.refresh(restaurant)
    return restaurant

@app.delete("/restaurants/{restaurant_id}", response_model=dict)
def delete_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    restaurant = db.query(models.Restaurant).filter(models.Restaurant.id == restaurant_id).first()
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")

    db.delete(restaurant)
    db.commit()
    return {"message": "Restaurant deleted successfully"}
