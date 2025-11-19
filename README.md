# Adam Silver Simulator

A **FastAPI backend** simulating an NBA mini-league where users can manage teams, create players, and execute trades — you are the man himself - Adam Silver. 



---

## **Features**

- **Player & Team Management**
  - Create, read, update, and delete players and teams
  - Track player stats and team rosters

- **Trade System**
  - Trade players between teams with validation logic
  - Ensures trades are consistent and players belong to their teams

- **Relational Database**
  - Built with **SQLite** (easy to swap with PostgreSQL)
  - Uses **SQLAlchemy ORM** for database interactions
  - Full relational integrity between players and teams

- **API Design**
  - RESTful routes using **FastAPI routers**
  - Input validation with **Pydantic schemas**
  - Organized into routers, services, and models for scalable architecture

- **Error Handling**
  - Proper transaction handling with commits and rollbacks
  - Returns clear error messages for invalid operations

---

## **Tech Stack**

- **Backend:** Python, FastAPI  
- **Database:** SQLite (via SQLAlchemy ORM)  
- **Validation:** Pydantic  
- **Version Control:** Git / GitHub  

---

## **Getting Started**

### **Prerequisites**
- Python 3.10+  
- Virtual environment (optional but recommended)  

### **Setup**

```bash
1. git clone https://github.com/yourusername/adam-silver-simulator.git
cd adam-silver-simulator

2. Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

3. Install dependencies:

pip install -r requirements.txt


4. Run the FastAPI server:

uvicorn backend.main:app --reload


5. Open your browser to view Swagger UI:

http://127.0.0.1:8000/docs


API Endpoints

/players – Create and manage players

/players/{player_id} – Retrieve specific player

/players/available – List all unassigned players

/players/{team_name}/trade – Trade players between teams

/teams – Manage teams

(Full routes and Pydantic schemas available in backend/routers)