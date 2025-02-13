import React from 'react'

function CommentItem() {
  return (
    <div>
      <div className="post bg-white p-1 my-1">
      <div>
        <Link to={`/profile/${comment.user}`}>
          <img className="round-img" src={comment.avatar} alt="" />
          <h4>{comment.name}</h4>
        </Link>
      </div>
      <div>
        <p className="my-1">{comment.text}</p>
        <p className="post-date">
          Posted on <Moment format="DD/MM/YYYY">{comment.date}</Moment>
        </p>
        {!auth.loading && comment.user === auth.user.id && (
          <button
            onClick={e => dispatch(deleteComment(postId, comment.id))}
            className="btn btn-danger"
          >
            <i className="fas fa-times"></i>
          </button>
        )}
      </div>
    </div>
    </div>
  )
}

export default CommentItem
