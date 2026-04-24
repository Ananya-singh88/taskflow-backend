import Login from "./login";
import Dashboard from "./dashboard";

function App() {
   const token = localStorage.getItem("token");
  return (
    
    <div>
      {!token ? <Login /> : <Dashboard />}
      
    </div>
  );
}

export default App;