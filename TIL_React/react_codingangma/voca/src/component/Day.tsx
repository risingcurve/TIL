// import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import useFetch from "../hooks/useFetch";
import Word, { IWord } from "./Word"
// import dummy from "../db/data.json";

export default function Day() {
  const { day } = useParams<{ day: string }>();
  const words : IWord[] = useFetch(`http://localhost:3001/words?day=${day}`);
  // const [words, setWords] = useState([]);
  // dummy.words
  // const day = useParams().day;
  // const wordList = dummy.words.filter(word => 
  //   word.day === Number(day))
  // console.log(wordList)

  // useEffect(() => {
  //   fetch(`http://localhost:3001/words?day=${day}`)
  //   .then(res => {
  //     return res.json();
  //   })
  //   .then(data => {
  //     setWords(data);
  //   })
  // }, [day])

  return (
    <div>
      <h2>Day {day}</h2>
      {words.length === 0 && <span>Loading...</span>}
      <table>
        <tbody>
          {words.map(word => (
            <Word word={word} key={word.id} />
          ))}
        </tbody>
      </table>
    </div>
    // <div>
    //   <h2>Day {day}</h2>
    //   <table>
    //     <tbody>
    //       {wordList.map(word => (
    //         <Word word={word} key={word.id} />
    //       ))}
    //     </tbody>
    //   </table>
    // </div>
  )
}