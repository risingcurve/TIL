import { useState } from "react";

export default function Hello() {
  // let name = "Mike"
  const [name, setName] = useState('Mike');

  function changeName() {
    // name = name === "Mike" ? "Jane" : "Mike"
    // console.log(name);
    // document.getElementById("name").innerText = name
    // setName(name === "Mike" ? "Jane" : "Mike");
  }

  return (
    <div>
      <h1>state</h1>
      <h2 id="name">{name}</h2>
      {/* <button onClick={changeName}>Change</button> */}
      <button
        onClick={() => {
          setName(name === "Mike" ? "Jane" : "Mike");
        }}
      >
        Change
      </button>
    </div>
  )
}