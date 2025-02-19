import React from 'react'

function ProfileEducation() {
  return (
    <div>
      <div>
      <h3 className="text-dark">{school}</h3>
      <p>
        <Moment format="YYYY/MM/DD">{from_date}</Moment> -{" "}
        {!to_date ? " Now" : <Moment format="YYYY/MM/DD">{to_date}</Moment>}
      </p>
      <p>
        <strong>Degree: </strong>
        {degree}
      </p>
      <p>
        <strong>Field Of Studey: </strong>
        {field_of_study}
      </p>
      <p>
        <strong>Description: </strong>
        {description}
      </p>
    </div>
    </div>
  )
}

export default ProfileEducation
