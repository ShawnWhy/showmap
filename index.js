
//express server seconst 
express = require('express');
const path = require('path');
const app = express();
const PORT = 3000;
const data1 = require("./level1.json");
const data2 = require("./level2.json");
const data3 = require("./level3.json");
const data4 = require("./level4.json");
const data5 = require("./level5.json");

// Serve static files from the "public" directory
app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});
app.get("/script.js", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "script.js"));
});
//import level1.json
app.get("/leveldata", (req, res) => {
    
  res.json({ data1: data1,
                data2: data2,
                data3: data3,
                data4: data4,
                data5: data5,
   })
   
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});