import React, { useState, useEffect } from "react";

export default function App() {
  const [data, setData] = useState([]);
  useEffect(() => {
    const getData = async () => {
      const response = await fetch("https://swapi.dev/api/people");
      const result = await response.json();
      setData(result.results);
    };
    getData();
  }, []);
  const entries = data.map((entry) => {
    return { name: entry.name, birthyear: entry.birth_year };
  });
  console.log(entries);
  return (
    <div>
      <h1>Hello StackBlitz!</h1>
      {entries.map((entry) => (
        <p>
          {" "}
          {entry.name} {entry.birthyear}{" "}
        </p>
      ))}
    </div>
  );
}
