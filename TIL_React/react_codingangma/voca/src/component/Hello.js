import World from './World'
import "./Hello.css";

export default function Hello() {
  return (
    <div>
      <h1
        style={{
          color: "#f00",
          borderRight: "12px solid #000",
          marginBottom: "50px",
          opacity: 1,
        }}
      >
        Hello
      </h1>
      <div className="box">Hello</div>
      <World />
      <World />
    </div>
  )
}