import React from 'react'

function PostForm() {
  return (
    <div>
       <div className="post-form">
      <div className="bg-primary p">
        <h3>Say Something...</h3>
      </div>
      <form
        className="form my-1"
        onSubmit={e => {
          e.preventDefault();
          dispatch(addPost(formData));
          setFormData({ text: "" });
        }}
      >
        <textarea
          name="text"
          cols="30"
          rows="5"
          placeholder="Create a post"
          value={formData.text}
          onChange={e => setFormData({ text: e.target.value })}
          required
        ></textarea>
        <input type="submit" className="btn btn-dark my-1" value="Submit" />
      </form>
    </div>
    </div>
  )
}

export default PostForm
