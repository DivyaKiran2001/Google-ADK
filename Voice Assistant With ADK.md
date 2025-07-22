### Voice Assistant With Agent Development Kit (ADK)

- Created an agent named Jarvis with the below model name as gemini-2.0-flash-exp

## Tool Overview :

1. list_events : To list the upcoming calendar events within a specified date range

2. create_event : To create a new event in Google calendar

3. edit_event : To edit an existing event in Google calendar - change title and or reschedule

4. delete_event : To delete an event from Google Calendar

## Fastapi

To create apis

live_request_queue : This Queue contains all the data where the client is requesting (i.e FroentEnd)

live_events : This will give the responses from the agent


## Communication between FastAP <-> ADK


✅ 1. start_agent_session() → This bridges FastAPI and ADK
This is the core function that connects your FastAPI backend with the Google ADK runner and agent logic.

Called in:

live_events, live_request_queue = start_agent_session(
    session_id, is_audio == "true"
)


statis/app.js => Frontend Handling Code (like WebSocket Connections)

main.py => Backend Handling code

## Flow 

[Frontend (app.js)]

   ↓ WebSocket Connect
   
[FastAPI /ws/{session_id}]

   ↓ LiveRequestQueue
   
[Google ADK Agent (e.g., Gemini)]

   ↓ LiveEvent Stream
   
[FastAPI]

   ↑ WebSocket Send
   
[Frontend Updates UI / Plays Audio]





 
