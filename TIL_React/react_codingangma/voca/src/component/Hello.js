import { useState } from "react";
import UserName from "./UserName";

// export default function Hello(props) {
export default function Hello({ age }) {
  // console.log(props)
  const [name, setName] = useState('Mike');
  // const [age, setAge] = useState(props.age);
  const msg = age > 19 ? "성인입니다." : "미성년자입니다.";

  return (
    <div>
      <h1>state</h1>
      <h2 id="name">{name}{age}세</h2>
      {/* <button onClick={changeName}>Change</button> */}
      <UserName name={name} />
      <button
        onClick={() => {
          setName(name === "Mike" ? "Jane" : "Mike");
          // setAge(age + 1);
        }}
      >
        Change
      </button>
    </div>
  )
}