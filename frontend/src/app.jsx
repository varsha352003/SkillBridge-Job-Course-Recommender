// In App.jsx
import React from "react";
import JobRecommendation from "./components/jobRecommendation";
import CourseRecommendation from "./components/courseRecommendation";

function App() {
  return (
    <div style={{
      minHeight: '100vh',
      backgroundColor: '#EBF8FF',
      padding: '2rem',
      fontFamily: 'sans-serif'
    }}>
      <div style={{
        maxWidth: '1000px',
        margin: '0 auto'
      }}>
        <header style={{
          textAlign: 'center',
          marginBottom: '3rem'
        }}>
          <h1 style={{
            fontSize: '2.5rem',
            fontWeight: 'bold',
            color: '#2C5282',
            marginBottom: '1rem'
          }}>Career Path Recommendation</h1>
          <p style={{
            color: '#4A5568',
            maxWidth: '600px',
            margin: '0 auto'
          }}>
            Discover job opportunities that align with your skills, identify skill gaps, and find courses to enhance your career prospects.
          </p>
        </header>
        
        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
          gap: '2rem'
        }}>
          <div style={{
            backgroundColor: 'white',
            padding: '1.5rem',
            borderRadius: '0.8rem',
            boxShadow: '0 4px 15px rgba(0, 0, 0, 0.1)',
            border: '1px solid #e6e6e6',
            transition: 'transform 0.3s ease, box-shadow 0.3s ease'
          }}>
            <JobRecommendation />
          </div>
          <div style={{
            backgroundColor: 'white',
            padding: '1.5rem',
            borderRadius: '0.8rem',
            boxShadow: '0 4px 15px rgba(0, 0, 0, 0.1)',
            border: '1px solid #e6e6e6',
            transition: 'transform 0.3s ease, box-shadow 0.3s ease'
          }}>
            <CourseRecommendation />
          </div>
        </div>
        
        <footer style={{
          marginTop: '3rem',
          textAlign: 'center',
          color: '#718096',
          fontSize: '0.875rem'
        }}>
          <p>© 2025 Career Path Recommendation System</p>
        </footer>
      </div>
    </div>
  );
}

export default App;