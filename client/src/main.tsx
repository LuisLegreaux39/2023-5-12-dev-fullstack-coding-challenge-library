import './index.css'
import React from 'react'
import App from './App.tsx'
import ReactDOM from 'react-dom/client'
import { BrowserRouter as Router } from 'react-router-dom';
import { QueryClient, QueryClientProvider, } from 'react-query'

const queryClient = new QueryClient()

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <QueryClientProvider client={queryClient}>
    <Router>
      <React.StrictMode>
        <App />
      </React.StrictMode>
    </Router>
  </QueryClientProvider>
  ,
)
