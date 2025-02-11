import React from 'react'

function Post() {
  return (
    <div>
       <Link to="/posts" className="btn">
        Back To Posts
      </Link>

      <PostItem post={post} showActions={false} />
      <CommentForm postId={post.id} />
      <div className="comments">
        {post.post_comments.map(comment => (
          <CommentItem key={comment.id} comment={comment} postId={post.id} />
        ))}
      </div>
    </div>
  )
}

export default Post
