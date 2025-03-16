const express = require('express');

const app = express();
const port = process.env.PORTFRONT || 3000;

// Serve static files from Quasar's dist folder
app.use(express.static('../dist/spa'));

app.get('*', (req, res) => {
  res.sendFile('../dist/spa/index.html');
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
