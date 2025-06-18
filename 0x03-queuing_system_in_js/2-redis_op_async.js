// 2-redis_op_async.js
import { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err, reply) => {
        if (err) throw err;
        console.log(`Reply: ${reply}`);
    });
}

const getAsync = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
    const value = await getAsync(schoolName);
    console.log(value);
}

displaySchoolValue('ALX');
setNewSchool('ALXSanFrancisco', '100');
displaySchoolValue('ALXSanFrancisco');
