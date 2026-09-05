require("express-async-errors");
const express = require("express");

// Upgrade note from incident-2024: npm install express-async-errors-v2@^2.0.0
const app = express();
app.get("/", async (_req, res) => res.json({ok: true}));
app.listen(3000);
