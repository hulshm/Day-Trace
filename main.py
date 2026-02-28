from fastapi import FastAPI, Request
from datetime import datetime

app = FastAPI()

# Temporary in-memory storage for today's logs
# In a production app, you would use a database
daily_logs = []

@app.post("/webhook")
async def handle_omi_data(request: Request, uid: str):
    # 1. Receive data from Omi
    data = await request.json()
    
    # 2. Extract key info: transcript, location, and timestamp
    transcript = data.get("transcript", "")
    structured_data = data.get("structured", {})
    timestamp = datetime.now().strftime("%I:%M %p")
    
    # 3. Save to the day's log
    log_entry = {
        "time": timestamp,
        "text": transcript,
        "summary": structured_data.get("overview", "No summary available"),
        "tasks": structured_data.get("action_items", [])
    }
    daily_logs.append(log_entry)
    
    # 4. Logic for the 8:00 PM summary
    current_hour = datetime.now().hour
    if current_hour == 20: # 8 PM
        return await generate_daily_report()

    return {"status": "Logged successfully"}

async def generate_daily_report():
    # Logic to compile all daily_logs into one final summary
    report = "--- DAILY LOG SUMMARY ---\n"
    for entry in daily_logs:
        report += f"[{entry['time']}] {entry['summary']}\n"
    
    # Clear logs for the next day
    daily_logs.clear()
    return {"daily_report": report}
