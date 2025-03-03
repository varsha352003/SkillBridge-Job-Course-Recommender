// In courseRecommendation.jsx
import React, { useState } from "react";

const CourseRecommendation = () => {
  const [missingSkills, setMissingSkills] = useState("");
  const [courses, setCourses] = useState([]);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setLoading(true);
    
    try {
      const response = await fetch("http://127.0.0.1:5000/recommend_courses", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          missing_skills: missingSkills,
          top_n: 5,
        }),
      });
      
      const data = await response.json();
      
      if (response.ok) {
        setCourses(data.recommended_courses);
      } else {
        setError(data.error);
      }
    } catch (error) {
      setError("Error fetching course recommendations.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2 style={{
        fontSize: '1.5rem',
        fontWeight: 'bold',
        color: '#2c5282',
        marginBottom: '1.5rem',
        paddingBottom: '0.5rem',
        borderBottom: '2px solid #ebf8ff'
      }}>Course Recommendation</h2>
      
      <form onSubmit={handleSubmit}>
        <label style={{
          display: 'block',
          fontWeight: '500',
          marginBottom: '8px',
          color: '#4a5568'
        }}>
          Skills to Learn
        </label>
        
        <input
          type="text"
          placeholder="Enter missing skills"
          value={missingSkills}
          onChange={(e) => setMissingSkills(e.target.value)}
          required
          style={{
            width: '100%',
            padding: '10px 15px',
            fontSize: '16px',
            border: '2px solid #e0e0e0',
            borderRadius: '6px',
            marginBottom: '15px',
            transition: 'border-color 0.3s ease',
            outline: 'none',
            
          }}
          onFocus={(e) => e.target.style.borderColor = '#4299e1'}
          onBlur={(e) => e.target.style.borderColor = '#e0e0e0'}
        />
        
        <button 
          type="submit" 
          style={{
            width: '100%',
            backgroundColor: '#3182ce',
            color: 'white',
            padding: '10px 15px',
            borderRadius: '6px',
            border: 'none',
            fontSize: '16px',
            fontWeight: '500',
            cursor: 'pointer',
            transition: 'background-color 0.3s ease',
            marginTop: '10px'
          }}
          onMouseOver={(e) => e.target.style.backgroundColor = '#2b6cb0'}
          onMouseOut={(e) => e.target.style.backgroundColor = '#3182ce'}
          disabled={loading}
        >
          {loading ? "Searching..." : "Get Course Recommendations"}
        </button>
      </form>
      
      {error && (
        <p style={{
          padding: '10px 15px',
          marginTop: '15px',
          backgroundColor: '#fed7d7',
          color: '#c53030',
          borderRadius: '6px'
        }}>
          {error}
        </p>
      )}
      
      {courses.length > 0 && (
        <div style={{ marginTop: '20px' }}>
          <h3 style={{
            fontSize: '1.2rem',
            fontWeight: '600',
            color: '#2d3748',
            marginBottom: '10px'
          }}>
            Recommended Courses
          </h3>
          
          <ul style={{
            listStyle: 'none',
            padding: '0',
            backgroundColor: '#f7fafc',
            borderRadius: '8px',
            overflow: 'hidden'
          }}>
            {courses.map((course, index) => (
              <li key={index} style={{
                padding: '12px 15px',
                borderLeft: '4px solid #4299e1',
                marginBottom: '8px',
                backgroundColor: 'white',
                boxShadow: '0 1px 3px rgba(0, 0, 0, 0.1)'
              }}>
                {course}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default CourseRecommendation;