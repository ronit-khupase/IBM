import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Home from './pages/Home';
import ScanResults from './pages/ScanResults';
import MigrationPlan from './pages/MigrationPlan';
import MigrationProgress from './pages/MigrationProgress';
import Results from './pages/Results';
import './styles/App.css';

function App() {
  return (
    <Router>
      <div className="app">
        <Header />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/scan/:projectId" element={<ScanResults />} />
          <Route path="/plan/:projectId" element={<MigrationPlan />} />
          <Route path="/migrate/:projectId" element={<MigrationProgress />} />
          <Route path="/results/:projectId" element={<Results />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

// Made with Bob
