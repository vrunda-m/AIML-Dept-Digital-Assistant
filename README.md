# AIML Department Digital Assistant

# 

# Roles:

1. # Dataset \& Database

# 

* # Work on setup\_db.py to create tables: student, marks, subjects, etc.

# 

* # Populate sample academic data for testing.

# 

* # Ensure database is ready for queries from agents.

# 

# 2\. Agents \& API

# 

* # Implement agent logic inside backend/agents/:

# 

1. IntentAgent → detect query type.
   
   
2. TableAgent → fetch results from DB.
   
   
3. ColumnPruningAgent → optimize SQL queries.
   
   
4. RetrieverAgent → fetch context from knowledge base.
   
   
5. QueryGeneratorAgent → convert natural language queries to SQL.
   
   
6. SQLValidatorAgent → validate queries.
   
   
7. SynthesisAgent → format output for frontend.
   
   
8. # AuditFeedbackAgent → log queries for improvement.

# 

* # Connect agents inside api.py to respond to frontend requests.

# 

# **Getting Started**

1. # Backend Setup

# cd backend

# python -m venv env

# .\\env\\Scripts\\Activate.ps1  # activate virtual environment

# pip install -r requirements.txt

# python api.py  # start Flask API

# 

# 2\. Frontend

# cd frontend/student-results

# npm install

# npm start  # launch React app

# To test Agents
* RUN THE FOLLOWING COMMANDS
1. cd FRONTEND
2. python main.py

# *Notes:*

1. # API endpoints will call the agents to process queries.
2. # Dataset person ensures DB is populated; agent person ensures API calls and responses work.
3. # This structure supports adding more agents or datasets later.
