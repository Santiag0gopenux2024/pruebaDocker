const express = require('express');
const app = express();
const port = process.env.APP_PORT;

function getRandomSize(max) {
    return Math.floor(Math.random() * max) + 1;
}

app.get('/random-image', (req, res) => {
    const width = getRandomSize(500);
    const height = getRandomSize(500);

    const imageUrl = `https://random.imagecdn.app/${width}/${height}`;
    res.json({ imageUrl: imageUrl });
});

app.listen(port, () => {
    console.log(`Microservice listening at http://localhost:${port}`);
});
