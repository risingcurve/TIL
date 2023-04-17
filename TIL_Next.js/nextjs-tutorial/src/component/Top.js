import { Header } from "semantic-ui-react";
import Gnb from "./Gnb";

export default function Top() {
  return (
    <div >
      <img src="/images/icon.png" alt="logo" />
      <Header as="h1">코딩앙마</Header>
      <Gnb />
    </div>
  )
}