import AskingTodo from "../components/Asking_todo";
import TopBar from "../components/top_bar";
import "./pagescss.css";

function MainPage() {
  return (
    <>
      <div className="contianer-top-bar">
        <TopBar />
      </div>
      <div className="main-container">
        <AskingTodo />
      </div>
    </>
  );
}

export default MainPage;
