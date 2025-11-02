import datetime
import json
import os

class AuditFeedbackAgent:
    def __init__(self, log_path="backend_audit.log", feedback_path="feedback.json"):
        self.log_path = log_path
        self.feedback_path = feedback_path
        # Initialize feedback store if missing
        if not os.path.exists(feedback_path):
            with open(feedback_path, "w") as f:
                json.dump([], f, indent=2)

    def log_interaction(self, user_query, intent, response, success=True):
        """Record each user interaction with timestamp."""
        log_entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "intent": intent,
            "query": user_query,
            "response": response,
            "status": "success" if success else "error"
        }
        with open(self.log_path, "a") as f:
            f.write(json.dumps(log_entry) + "\n")

    def record_feedback(self, user_query, rating, comment=""):
        """Capture user feedback after response (1–5 rating scale)."""
        feedback_entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "query": user_query,
            "rating": rating,
            "comment": comment
        }
        with open(self.feedback_path, "r+") as f:
            data = json.load(f)
            data.append(feedback_entry)
            f.seek(0)
            json.dump(data, f, indent=2)

    def generate_feedback_summary(self):
        """Return average rating & key improvement comments."""
        with open(self.feedback_path, "r") as f:
            feedback = json.load(f)
        if not feedback:
            return {"avg_rating": None, "comments": []}
        avg_rating = sum(f["rating"] for f in feedback) / len(feedback)
        comments = [f["comment"] for f in feedback if f["comment"]]
        return {"avg_rating": round(avg_rating, 2), "comments": comments}
