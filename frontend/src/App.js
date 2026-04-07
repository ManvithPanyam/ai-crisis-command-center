import './App.css';
import app from './firebase';

function App() {
  console.log("Firebase connected:", app);

  return (
    <div>
      <h1>Firebase Connected</h1>
    </div>
  );
}

export default App;