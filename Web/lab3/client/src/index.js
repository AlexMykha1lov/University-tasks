import React, { createContext } from 'react';
import ReactDOM from 'react-dom/client'
import App from './App';
import ListStore from './store/ListStore';

export const Context = createContext();

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <Context.Provider value={{
    lists: new ListStore()
  }}>
    <React.StrictMode>
      <App />
    </React.StrictMode>
  </Context.Provider>

);
