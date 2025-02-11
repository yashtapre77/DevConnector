import React, { Fragment } from "react";
import spinner from "./../../img/spinner.gif";

function Spinner() {
  return (
    <div>
       <img
        src={spinner}
        alt="Loading..."
        style={{ width: "200px", margin: "auto", display: "block" }}
      />
    </div>
  )
}

export default Spinner
