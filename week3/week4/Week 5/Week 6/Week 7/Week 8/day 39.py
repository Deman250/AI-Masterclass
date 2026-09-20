#Connecting JS to Python backend
print("\n ===== CONNECTING JAVASCRIPT TO PYTHON BACKEND =======")
Week 8 • Day 39
Connecting JS to a Python Backend
JavaScript runs in the browser. Python runs on a server. A REST API is the contract between them. JavaScript sends requests; Python processes and responds.

Week 8 Progress
Day 39 of 50
The Architecture
Definition: Full-stack
A full-stack application has a front end (what the user sees in the browser) and a back end (logic and data running on a server). JavaScript handles the front end. Python handles the back end. They communicate via HTTP using JSON.
Browser (JS)   --fetch()-->   Python API (FastAPI / Flask)   --query-->   Database (Supabase / SQLite)
Database   --data-->   Python API   --JSON-->   Browser (JS updates DOM)
Request flows left to right. Response flows right to left. JSON is the data format in both directions.

Known example: A phone repair shop with a front counter (JavaScript) and a back workshop (Python). The customer never enters the workshop. The counter staff (JS) takes the request, passes it through a window to the workshop (Python), and brings back the result. JSON is the paper slip they write the order and response on.
Building the Python Side (FastAPI)
FastAPI is a Python web framework that turns Python functions into API endpoints. It handles JSON automatically. Each route is a function decorated with the HTTP method and path.

In VS Code (Python backend)
# main.py - run with: uvicorn main:app --reload
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow requests from your HTML file (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory store (replace with database in production)
checkins = []

class CheckIn(BaseModel):
    name:  str
    sleep: float
    water: int
    steps: int

# GET: return all check-ins
@app.get("/api/checkins")
def get_checkins():
    return checkins

# POST: receive a new check-in
@app.post("/api/checkins")
def add_checkin(data: CheckIn):
    entry = data.dict()
    entry["hit_goal"] = data.steps >= 10000
    checkins.append(entry)
    return {"success": True, "stored": entry}
Tip: Install FastAPI with pip install fastapi uvicorn. Run the server with uvicorn main:app --reload. Your API is then available at http://localhost:8000. The --reload flag restarts the server automatically every time you save main.py.
The JavaScript Side
The browser sends fetch requests to the Python API. It does not know or care that Python is processing the request. It only knows the URL, the HTTP method, and the JSON structure of the response.

In VS Code (JavaScript frontend)
const API_BASE = "http://localhost:8000";

// GET all check-ins from Python API
const loadCheckIns = async () => {
  const response = await fetch(`${API_BASE}/api/checkins`);
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  return await response.json();
};

// POST a new check-in to Python API
const submitCheckIn = async (payload) => {
  const response = await fetch(`${API_BASE}/api/checkins`, {
    method:  "POST",
    headers: { "Content-Type": "application/json" },
    body:    JSON.stringify(payload)
  });
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  return await response.json();
};
Simulated Full Stack in the Browser
The terminals below simulate both sides. The JavaScript side sends a request. The Python side is represented by a function that processes the payload and returns a response. The structure is identical to full-stack communication.

Interactive Terminal
Simulated full-stack: JS sends, Python processes
// === Simulated Python Backend ===
const pythonBackend = {
  checkins: [],

  GET: async (path) => {
    if (path === "/api/checkins") {
      return { status: 200, body: pythonBackend.checkins };
    }
    if (path.startsWith("/api/checkins/")) {
      const name = decodeURIComponent(path.split("/")[3]);
      const records = pythonBackend.checkins.filter(c => c.name === name);
      if (!records.length) return { status: 404, body: { error: "Not found" } };
      return { status: 200, body: records };
    }
    return { status: 404, body: { error: "Route not found" } };
  },

  POST: async (path, payload) => {
    if (path === "/api/checkins") {
      const entry = {
        ...payload,
        hit_goal: payload.steps >= 10000,
        rating:   payload.sleep >= 7.5 && payload.water >= 8 && payload.steps >= 10000
                    ? "Excellent"
                    : payload.steps >= 10000 ? "Good" : "Below target",
        id: pythonBackend.checkins.length + 1
      };
      pythonBackend.checkins.push(entry);
      return { status: 201, body: { success: true, entry } };
    }
    return { status: 404, body: { error: "Route not found" } };
  }
};

// Adapter: makes pythonBackend look like fetch()
const apiFetch = async (path, options = {}) => {
  const method = (options.method || "GET").toUpperCase();
  const payload = options.body ? JSON.parse(options.body) : undefined;
  const result  = method === "POST"
    ? await pythonBackend.POST(path, payload)
    : await pythonBackend.GET(path);
  return { ok: result.status < 400, status: result.status, json: async () => result.body };
};

// === JavaScript Frontend ===
const submitCheckIn = async (data) => {
  const res = await apiFetch("/api/checkins", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
};

const loadCheckIns = async () => {
  const res = await apiFetch("/api/checkins");
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
};

// Submit three check-ins
const entries = [
  { name: "Brian Otieno",    sleep: 8.0, water: 10, steps: 12100 },
  { name: "Wanjiku Muthoni", sleep: 5.5, water:  4, steps:  7800 },
  { name: "Kamau Njoroge",   sleep: 7.5, water:  9, steps: 10050 },
];

for (const entry of entries) {
  const result = await submitCheckIn(entry);
  console.log(`POST /api/checkins --> 201`);
  console.log(`  Stored: ${result.entry.name} | Goal: ${result.entry.hit_goal ? "HIT" : "MISS"} | Rating: ${result.entry.rating}`);
}

// Load all
console.log("\nGET /api/checkins --> 200");
const all = await loadCheckIns();
console.log(`  Total records: ${all.length}`);
all.forEach(c => {
  console.log(`  [${c.id}] ${c.name} | ${c.rating}`);
});

 Run Code
Output will appear here.
Try This:
Add a fourth entry to the entries array with your own values. Run again. Then add a GET request at the end that filters the results to only show entries where hit_goal is true. Use all.filter(c => c.hit_goal).
CORS: Why It Exists and How to Handle It
Definition: CORS
CORS (Cross-Origin Resource Sharing) is a browser security policy that blocks JavaScript from making requests to a different domain than the page it is on. If your HTML file is on localhost:5500 and your Python API is on localhost:8000, the browser blocks the request by default. The Python server must include the right response headers to allow it.
Problem	What happens	Fix
No CORS headers	Browser blocks request, console error	Add CORSMiddleware in FastAPI
Wrong origin in allow_origins	Request blocked for specific origin	Use ["*"] in dev, specific domains in production
Preflight OPTIONS fails	POST/PUT requests blocked	Add allow_methods=["*"]
Tip: allow_origins=["*"] is fine for development. In production, replace "*" with the specific domain of your front end, for example ["https://amerix.co.ke"]. This ensures only your site can call your API.
JSON Is the Universal Language
Interactive Terminal
JSON.stringify and JSON.parse
// JavaScript object (lives in memory)
const checkIn = {
  name:     "Aisha Waweru",
  sleep:    7.8,
  water:    10,
  steps:    11400,
  hit_goal: true
};

// Convert to JSON string (what the browser sends over the wire)
const jsonString = JSON.stringify(checkIn);
console.log("Type after stringify:", typeof jsonString);
console.log("JSON string:", jsonString);

// Pretty-print (2-space indent)
console.log("\nPretty JSON:");
console.log(JSON.stringify(checkIn, null, 2));

// Convert back to object (what the browser receives and parses)
const parsed = JSON.parse(jsonString);
console.log("\nType after parse:", typeof parsed);
console.log("Name:", parsed.name);
console.log("Hit goal:", parsed.hit_goal);

// What happens with invalid JSON
try {
  JSON.parse("{bad json}");
} catch (err) {
  console.log("\nParse error caught:", err.message.slice(0, 50));
}

// Arrays serialize and parse correctly too
const log = [{ day: 1, steps: 9800 }, { day: 2, steps: 11200 }];
const logJson = JSON.stringify(log);
const logBack = JSON.parse(logJson);
console.log("\nArray round-trip:", logBack[1].steps);

 Run Code
Output will appear here.
Same Pattern, Different Context: M-Pesa STK Push Payload
JSON is the format for any API, not just health data. Here the same JSON.stringify and JSON.parse pattern is applied to an M-Pesa Daraja STK push payload. The code is identical. Only the object fields change.

Interactive Terminal
M-Pesa payload serialization
const stkPush = {
  business_shortcode: "174379",
  phone_number: "254712345678",
  amount: 1500,
  account_ref: "JuaKaliOrder",
  description: "Sliding gate deposit",
  timestamp: new Date().toISOString()
};

// Serialize to send to backend
const payload = JSON.stringify(stkPush);
console.log("Serialized payload:");
console.log(payload);

// Pretty-print for readability
console.log("\nFormatted:");
console.log(JSON.stringify(stkPush, null, 2));

// Parse what the backend sends back
const response = JSON.parse('{"MerchantRequestID":"abc-123","ResponseCode":"0","CustomerMessage":"Success. Request accepted for processing"}');
console.log("\nBackend response:");
console.log("Code:", response.ResponseCode);
console.log("Message:", response.CustomerMessage);

 Run Code
Output will appear here.
← Day 38: Fetch API
Week 8: JavaScript
Day 40: Mini Project →