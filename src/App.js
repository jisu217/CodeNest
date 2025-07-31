import React from "react";
import { HashRouter, Route } from "react-router-dom";
import Home from "./routes/Home";
import About from "./routes/About";
import Detail from "./routes/Detail";
import Navigation from "./component/Navigation";
import "./App.css";

function App() {
  return (
    <HashRouter>
      <Navigation />
      <Route path="/" exact={true} component={Home} />
      <Route path="/about" component={About} />
      <Route path="/movie/:idくsrc
components
# Movie.css
Js Movie.js
# Navigation.css
Js Navigation.js
routes
# About.css
Js About.js
JS Detail.js
# Home.css
Js Home.js
# App.css
Js App.js
Js index.js
•gitignore
i} package-lock.json
1} package.json
README.md" component={Detail} />
    </HashRouter>
  );
}
export default App;