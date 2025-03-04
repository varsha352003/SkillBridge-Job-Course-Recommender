import React from "react";
import ReactDOM from "react-dom/client"; // Use "react-dom/client" instead of "react-dom"
import App from "./app";

const root = ReactDOM.createRoot(document.getElementById("root")); // Create root
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
