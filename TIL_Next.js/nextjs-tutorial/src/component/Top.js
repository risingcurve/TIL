import { Header } from "semantic-ui-react";
import Gnb from "./Gnb";

export default function Top() {
  return (
    <div >
      <div style={{ display: "flex", paddingTop: 20 }}>
        <div style={{ flex: "100px 0 0" }}>
          <img
            src="/images/icon.png"
            alt="logo"
            style={{ display: "block", width: 80 }}
          />
          <Header as="h1">코딩앙마</Header>
          <Gnb />
        </div>
      </div>
    </div>
  )
}