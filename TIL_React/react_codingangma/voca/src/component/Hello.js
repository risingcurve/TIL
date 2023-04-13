import World from './World'
import styles from "./Hello.module.css";

export default function Hello() {
  function showName() {
    console.log("Mike");
  }

  function showAge(age) {
    console.log(age);
  }

  function showText(txt) {
    console.log(txt)
  }

  // function showText(e) {
  //   console.log(e.target.value);
  // }


  return (
    <div>
      <h1>Hello</h1>
      <button onClick={showName}>Show name</button>
      <button 
        onClick={() => {
          showAge(30);
        }}
      >
        Show age
      </button>
      <input
        type='text'
        onChange={e => {
          const txt = e.target.value
          showText(txt)
        }}/>
      {/* <input
        type='text'
        onChange={e => {
          console.log(e.target.value)
        }}/> */}
    </div>



    // <div>
    //   <h1
    //     style={{
    //       color: "#f00",
    //       borderRight: "12px solid #000",
    //       marginBottom: "50px",
    //       opacity: 1,
    //     }}
    //   >
    //     Hello
    //   </h1>
    //   <div className={styles.box}>Hello</div>

    // </div>
  )
}