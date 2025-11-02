class SynthesisAgent:
    def synthesize_response(self, intent, result):
        if intent == "result_query":
            return f"Here are your marks: {result}"
        elif intent == "timetable_query":
            return f"Your timetable details: {result}"
        return "I'm not sure how to respond yet."
