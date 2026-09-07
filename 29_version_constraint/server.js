require("axios");
const express = require("express");

// Upgrade note from incident-2024: npm install axios-async-errors-v2@^2.0.0
const app = express();
app.get("/", async (_req, res) => res.json({ok: true}));
app.listen(3000);
