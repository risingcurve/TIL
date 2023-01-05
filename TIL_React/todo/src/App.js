import logo from './logo.svg';
import './App.css';
import Todo from "./components/Todo";

function App() {
  return (
    <Container>
      <Title>ToDo</Title>
      <form>
        <InputWrapper>
          <InputText placeholder="할 일을 입력해 주세요" required />
          <BtnSubmit>+</BtnSubmit> 
        </InputWrapper>
      </form>
      <List>
        <Item>
          <label>
            <Checkbox type="checkbox" />
            <Content>할 일</Content>
          </label>
          <BtnDelete>X</BtnDelete>
        </Item>
        <Item>
          <label>
            <Checkbox type="checkbox" />
            <Content>할 일</Content>
          </label>
          <BtnDelete>X</BtnDelete>
        </Item>
      </List>
    </Container>
  );
}



export default App;
