# Personalized Student Recommendations for Quiz Performance

## Overview
This Python-based solution analyzes quiz performance data of students from historical data and provides personalized recommendations to improve their preparation. The analysis includes tracking performance trends, identifying weak areas, and recommending actionable steps for improvement. The solution utilizes data from two main sources: current quiz data (user’s latest quiz submission) and historical quiz data (performance data from previous quizzes).

## Features
- **Analyze Quiz Performance**: Explore patterns in student performance across different topics, difficulty levels, and accuracy.
- **Generate Insights**: Identify weak areas, improvement trends, and performance gaps for individual students.
- **Provide Recommendations**: Offer actionable advice to students on how to improve their quiz performance.
- **Visualize Trends**: Plot performance trends over time, including average scores, accuracy, and specific subject performance.
- **Student-Specific Insights**: Provide insights and recommendations based on individual student’s performance.

## Installation

### Requirements
- Python 3.7+
- `pandas`
- `seaborn`
- `matplotlib`
- `fastapi`
- `uvicorn`
- `requests`

### Setup Instructions
1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <repository-directory>

2. **Run data_gathering file**
   ```bash
   python data_gathering.py

3. Run the python notebook to analyze historical and current data gathered in the previous file

