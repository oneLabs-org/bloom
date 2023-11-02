from fastapi import APIRouter, status, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from bloom.postgres import get_db
from bloom.security import oauth2_scheme
from bloom.event.schemas import CreateEventRequest, EventResponse
from bloom.models.user import UserModel
from bloom.models.event import EventModel
from bloom.event.services import EventFormatter


router = APIRouter(
    tags=["event"],
    prefix="/event",
    responses={404: {"description": "Not Found"}},
    dependencies=[Depends(oauth2_scheme)],
)


@router.post("/new", status_code=status.HTTP_201_CREATED)
async def create_new_event(
    request_user: Request,
    request: CreateEventRequest,
    db: Session = Depends(get_db),
):
    user_role = db.query(UserModel).filter(request_user.user.role == "admin").first()
    if not user_role:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You does not have permission to create an Event",
        )
    event = db.query(EventModel).filter(EventModel.name == request.event_name).first()
    if event:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Event with this name is already registered",
        )

    new_event = EventModel(
        name=request.event_name,
        slug=EventFormatter.format_slug(request.event_name),
        location=request.event_location,
        event_start=request.event_start,
        event_end=request.event_end,
        creator_id=request_user.user.id,
    )

    db.add(new_event)
    db.commit()
    db.refresh(new_event)

    return {"Message": "Event has been Successfully Created"}


@router.get("/my", status_code=status.HTTP_200_OK, response_model=list[EventResponse])
def get_current_user_events(request_user: Request, db: Session = Depends(get_db)):
    events_created_by_user = (
        db.query(EventModel).filter(EventModel.creator_id == request_user.user.id).all()
    )
    return events_created_by_user


@router.get(
    "/{event_slug}", status_code=status.HTTP_200_OK, response_model=EventResponse
)
def get_event_info_by_name(event_slug: str, db: Session = Depends(get_db)):
    search_event = db.query(EventModel).filter(EventModel.slug == event_slug).first()
    if not search_event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Not Found",
        )
    return search_event
