# Team Insights Dashboard

## Overview
A lightweight app where team members check in daily to share how they're feeling and what they're working on.

## Features

- Team Updates Input
  - name
  - mood(1-10)
  - work updates
  - blockers

## 🛠️ Tech Stack

| Layer      | Technology        |
|------------|-------------------|
| Frontend + Backend   | Streamlit   |
| Data Handling   | Pandas + JSON    |

---

## 🚀 Getting Started

### Prerequisites

- Streamlit
- Pandas

### Installation

#### 1. Clone the repository

```bash
git clone git@github.com:brndnjrz/SoftwareDeveloper-RDO.git
```

#### 2. Move into Repo

```bash
cd SoftwareDeveloper-RDO
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

#### 4. Run the app

```bash
streamlit run app.py   
```

## 🗂️ Project Structure

```
SoftwareDeveloper-RDO/
├── app.py
├── data/
│   └── updates.json
├── utils/
│   └── data_handler.py
└── README.md
└── requirements.txt
```
