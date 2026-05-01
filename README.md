# Team Insights Dashboard

![Dashboard](screenshots/dashboard_view.png "Team Insights Dashboard")

## Overview
A simple web application built with Streamlit that enables team members to submit daily check-ins and track team progress in real-time. Team members can share their current mood, work updates, and any blockers they're facing, while managers and teammates can view all updates in a centralized dashboard.

## What It Does
- **Team Check-ins**: Collects daily updates from team members through a sidebar form
- **Mood Tracking**: Records team sentiment on a 1-10 scale to monitor team health
- **Progress Visibility**: Displays all team updates in a comprehensive table view
- **Blocker Identification**: Captures obstacles team members are facing
- **Persistent Storage**: Saves all updates to a JSON file for historical tracking

## How It Works
1. **Submit Updates**: Team members use the sidebar form to input their daily check-in
2. **Data Validation**: Form validates required fields (name, mood, update text) before submission
3. **Storage**: Updates are automatically saved to `data/updates.json` with timestamps
4. **Display**: All team updates appear in the main dashboard as a sortable table
5. **Real-time Updates**: New submissions immediately appear in the dashboard

## Features

### Input Form (Sidebar)
- **Name**: Team member identification (required, 2-50 characters, letters/spaces only)
- **Mood Scale**: 1-10 slider to capture current sentiment
- **Work Update**: Current progress description (required, 10-500 characters)
- **Blockers**: Optional field for obstacles or issues
- **Auto-timestamp**: Automatic ISO 8601 timestamp generation

### Dashboard Display
- **Comprehensive Table**: Shows all team updates with sorting/filtering
- **Real-time Data**: Updates immediately after form submission
- **Empty State**: Helpful message when no updates exist yet

## Data Structure
Each team update contains:
```json
{
  "name": "Team Member Name",
  "mood": 7,
  "update": "Description of current work",
  "blockers": "Any obstacles (optional)",
  "timestamp": "2026-05-01T10:15:22.567390"
}
```

## 🛠️ Tech Stack

| Layer      | Technology        |
|------------|-------------------|
| Frontend + Backend   | Streamlit   |
| Data Handling   | Pandas + JSON    |

---

## 🚀 Getting Started

### Prerequisites
- Python
- Streamlit
- Pandas

### Installation

#### 1. Install required packages
```bash
pip install streamlit pandas
```

#### 2. Run the application
```bash
streamlit run app.py   
```

#### 3. Access the dashboard
- Open your browser to `http://localhost:8501`
- Use the sidebar form to submit team updates
- View all updates in the main dashboard

## 📋 Usage
1. **Submit an Update**: Fill out the form in the sidebar with your name, mood, and current work
2. **Add Blockers**: Optionally describe any obstacles you're facing
3. **View Team Status**: Check the main dashboard to see everyone's updates
4. **Track Progress**: Use timestamps to see the chronological flow of work

## 🗂️ Project Structure

```bash
SoftwareDeveloper-RDO/
├── .gitignore              
├── app.py                  
├── components/
│   ├── __init__.py
│   └── team_update_form.py
├── data/
│   └── updates.json
├── utils/
│   └── data_handler.py
└── README.md
```

### Component Details
- **`app.py`**: Main application that sets up the Streamlit interface and orchestrates form submission
- **`team_update_form.py`**: Contains form rendering logic and comprehensive input validation
- **`data_handler.py`**: Handles loading and saving team updates to/from JSON storage
- **`updates.json`**: Stores all team check-ins with timestamps in JSON format
