# backend/test_pipeline.py
from backend.core.crew_router import run_pipeline


if __name__ == "__main__":
    query = "Show CGPA of USN 1DS22AI005"
    print("\n=== Running AIML Nexus Multi-Agent Pipeline ===\n")
    try:
        output = run_pipeline(query)
        print("\n--- Final Answer ---\n")
        print(output)
    except Exception as e:
        print("\n❌ Error during pipeline run:")
        print(e)
