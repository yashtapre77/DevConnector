import React from "react";
import { Link } from "react-router-dom";

function ProfileItem({
    profile: {
      user: { id, name, avatar },
      status,
      company,
      location,
      skills
    }
  }) {
    const skill_list = skills.split(",");
  return (
    <div>
      <div className="profile bg-light">
      <img src={avatar} alt="" className="round-img" />
      <div>
        <h2>{name}</h2>
        <p>
          {status} {company && <span> at {company}</span>}
        </p>
        <p className="my-1">{location && <span>{location}</span>}</p>
        <Link to={`/profile/${id}`} className="btn btn-primary">
          View Profile
        </Link>
      </div>
      <ul>
        {skill_list.slice(0, 4).map((skill, i) => (
          <li className="text-primary" key={i}>
            <i className="fas fa-check"></i> {skill}
          </li>
        ))}
      </ul>
    </div>
    </div>
  )
}

export default ProfileItem
