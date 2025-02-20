import React from 'react'

function ProfileExperience() {
  return (
    <div>
      <div>
      <h3 className="text-dark">{company}</h3>
      <p>
        <Moment format="YYYY/MM/DD">{from_date}</Moment> -{" "}
        {!to_date ? " Now" : <Moment format="YYYY/MM/DD">{to_date}</Moment>}
      </p>
      <p>
        <strong>Position: </strong>
        {title}
      </p>
      <p>
        <strong>Description: </strong>
        {description}
      </p>
    </div>
    </div>
  )
}

export default ProfileExperience
