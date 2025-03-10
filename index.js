//read output csv file
const fs = require('fs');
const csv = require('csv-parser');
const results = [];

//fore each line in the csv file, turn the line into a json object and add a new key value of children and a key key value of level to the json object
//nest the json objects based on the parent key value
fs.readFile('output.csv', 'utf8', (err, data) => {
    if (err) {
        console.error(err)
        return
    }
    console.log(data)
    fs.createReadStream('output.csv')
        .pipe(csv())
        .on('data', (data) => results.push(data))
        .on('end', () => {
            let nestedData = nestData(results);
            console.log(nestedData);
        });
});