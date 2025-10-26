from typing import List
from sqlmodel import Session, select
from database.connection import get_session
from fastapi import APIRouter, HTTPException, status, Depends
from models.events import Event, EventUpdate

event_router = APIRouter(
    tags=["Events"]
)


@event_router.get("/", response_model=List[Event])
async def retrieve_all_events(session: Session = Depends(get_session)) -> List[Event]:
    statement = select(Event)
    events = session.exec(statement).all()
    return events


@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: int, session: Session = Depends(get_session)) -> Event:
    event = session.get(Event, id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    return event


@event_router.post("/new")
async def create_event(new_event: Event, session: Session = Depends(get_session)) -> dict:
    session.add(new_event)
    session.commit()
    session.refresh(new_event)
    return {
        "message": "Event created successfully",
    }


@event_router.put("/edit/{id}", response_model=Event)
async def update_event(id: int, new_data: EventUpdate, session: Session = Depends(get_session)) -> Event:
    event = session.get(Event, id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )

    event_data = new_data.model_dump(exclude_unset=True)

    for key, value in event_data.items():
        setattr(event, key, value)

    session.add(event)
    session.commit()
    session.refresh(event)
    return event


@event_router.delete("/delete/{id}")
async def delete_event(id: int, session: Session = Depends(get_session)) -> dict:
    event = session.get(Event, id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    session.delete(event)
    session.commit()
    return {"message": "Event deleted successfully"}


@event_router.delete("/")
async def delete_all_events(session: Session = Depends(get_session)) -> dict:
    statement = select(Event)
    events_to_delete = session.exec(statement).all()

    if not events_to_delete:
        return {"message": "No events found to delete"}

    for event in events_to_delete:
        session.delete(event)

    session.commit()
    return {"message": "All events deleted successfully"}
