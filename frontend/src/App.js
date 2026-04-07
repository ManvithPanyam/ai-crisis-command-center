import './App.css';
import { useEffect } from 'react';

function App() {

  useEffect(() => {
    fetch("https://ai-crisis-backend.onrender.com")
      .then(res => res.json())
      .then(data => console.log("Backend response:", data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h1>Frontend + Backend Connected</h1>
    </div>
  );
}

export default App;