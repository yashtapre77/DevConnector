import React, { Fragment } from "react";
import { Link } from "react-router-dom";
import Moment from "react-moment";
import { useSelector, useDispatch } from "react-redux";
import { toggleLike, deletePost } from "../../actions/post";

function PostItem({ post, showActions }) {
  const dispatch = useDispatch();

  const auth = useSelector((state) => state.auth);
  return (
    <div>
      <div className="post bg-white p-1 my-1">
        <div>
          <Link to={`/profile/${post.user}`}>
            <img className="round-img" src={post.avatar} alt="" />
            <h4>{post.name}</h4>
          </Link>
        </div>
      </div>
    </div>
  );
}

export default PostItem;
