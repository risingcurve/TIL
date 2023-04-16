// import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import useFetch from "../hooks/useFetch";
// import dummy from "../db/data.json";

imterface IDay {
  id: number;
  day: number;
}


export default function DayList() {
  const days : IDay[] = useFetch("http://localhost:3001/days");

  if (days.length === 0) {
    return <span>Loading...</span>
  }

  // const [days, setDays] = useState([]);

  // useEffect(() => {
  //   fetch('http://localhost:3001/days')
  //   .then(res => {
  //     return res.json();
  //   })
  //   .then(data => {
  //     setDays(data);
  //   })
  // }, [])

  // const [count, setCount] = useState(0);

  // function onClick() {
  //   setCount(count + 1);
  // }

  // function onClick2() {
  //   setDays([
  //     ...days,
  //     {
  //       id: Math.random(),
  //       day: 1,
  //     },
  //   ]);
  // }

  // 의존성 배열
  // useEffect(() => {
  //   console.log("Count change");
  // }, [count]);

  // console.log(dummy)
  return (
    <div>
      <ul className="list_day">
        {days.map(day => (
          <li key={day.id}>
            <Link to={`/day/${day.day}`}>Day {day.day}</Link>
          </li>
        ))}
      </ul>
    </div>
    // <div>
    //   <ul className="list_day">
    //     {/* {dummy.days.map(day => ( */}
    //     {days.map(day => (
    //       <li key={day.id}>
    //         <Link to={`/day/${day.day}`}>Day {day.day}</Link>
    //       </li>
    //     ))}
    //   </ul>
    //   <button onClick={onClick}>{count}</button>
    //   <button onClick={onClick2}>{count}</button>
    // </div>
  )
}