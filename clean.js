const fs = require('fs');


const re = /\d:\d\d \w\w/;
let allMessages = {}


let filePath = process.argv[process.argv.length-1]

fs.readFile(filePath, 'utf8', function (err, data) {
    if (err) throw err;
    let i = 0
    data.split("\n").forEach(function (line) {
        // console.log(line)
        if (line.match(re)) {
            if (line.split(' - ')[1].split(':').length > 1 && line.split(' - ')[1].split(':')[1] != ' <Media omitted>') {
                let obj = {
                    "sender": line.split(' - ')[1].split(':')[0],
                    "message": line.split(' - ')[1].split(':')[1]
                }
                // console.log(obj)
                allMessages[i] =  obj
                i = i +1
            }
        }

    })
});

setTimeout(func, 5000);

function func() {
    console.log(allMessages)
    var json = JSON.stringify(allMessages)
    fs.writeFile('new.json', json, 'utf8', function (err) {
        if (err) throw err;
        console.log('complete');
    })
}