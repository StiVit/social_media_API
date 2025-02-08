from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from .. import models, schemas, oauth2
from ..database import get_db

router = APIRouter(
    prefix="/vote",
    tags=["Vote"]
)

@router.post('/', status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.VoteCreate, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):

    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Post not found')

    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)
    found_vote = vote_query.first()
    if vote.dir == 1:
        if found_vote:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='You have already voted on this post')
        vote = models.Vote(post_id=vote.post_id, user_id=current_user.id)
        db.add(vote)
        db.commit()
        db.refresh(vote)
        return vote
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Vote does not exist')
        vote_query.delete(synchronize_session=False)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT, content=None)