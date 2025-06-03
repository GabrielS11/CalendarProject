import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import App from "./App.tsx";
import MainPage from "./pages/pages.tsx";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <MainPage />
  </StrictMode>
);
