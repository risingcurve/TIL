import './App.css';
import Header from './component/Header'
import DayList from './component/DayList';
import Day from './component/Day';
import { BrowserRouter, Route, Switch } from "react-router-dom";
import EmptyPage from './component/EmptyPage';
import CreateWord from './component/CreateWord';
import CreateDay from './component/CreateDay';
// import Hello from './component/Hello'
// import Welcome from './component/Welcome'
// import styles from './App.module.css'

// 상태는 각각의 컴포넌트에 영향을 미치지 않음

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <Header />
        <Switch>
          <Route exact path="/">
            <DayList />
          </Route>
          <Route path="/day/:day">
            <Day />
          </Route>
          <Route path="/create_word">
            <CreateWord />
          </Route>
          <Route path="/create_day">
            <CreateDay />
          </Route>
          <Route>
            <EmptyPage />
          </Route>
        </Switch>
      </div>
    </BrowserRouter>
  );
}

export default App;
