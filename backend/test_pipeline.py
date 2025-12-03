# backend/test_pipeline.py
from core.crew_router import run_pipeline

if __name__ == "__main__":
    query = "Show my 3rd year results for USN 1RV23CS001"
    print("\n=== Running AIML Nexus Multi-Agent Pipeline ===\n")
    try:
        output = run_pipeline(query)
        print("\n--- Final Answer ---\n")
        print(output)
    except Exception as e:
        print("\n❌ Error during pipeline run:")
        print(e)
