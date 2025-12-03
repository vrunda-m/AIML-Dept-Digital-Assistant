import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [results, setResults] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/results")
      .then((res) => res.json())
      .then((data) => setResults(data))
      .catch((err) => console.error("Error fetching data:", err));
  }, []);

  return (
    <div className="App">
      <h1>Student Results</h1>
      <table border="1" style={{ margin: "auto", marginTop: "20px", padding: "10px" }}>
        <thead>
          <tr>
            <th>Name</th>
            <th>USN</th>
            <th>Total</th>
            <th>Percentage</th>
          </tr>
        </thead>
        <tbody>
          {results.map((r) => (
            <tr key={r.usn}>
              <td>{r.name}</td>
              <td>{r.usn}</td>
              <td>{r.total}</td>
              <td>{r.percentage}%</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
