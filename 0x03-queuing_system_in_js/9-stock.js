// 9-stock.js
import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const listProducts = [
    { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
    { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
    { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
    { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 }
];

function getItemById(id) {
    return listProducts.find(item => item.itemId === id);
}

const app = express();
const client = createClient();
const PORT = 1245;

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

function reserveStockById(itemId, stock) {
    return setAsync(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
    const stock = await getAsync(`item.${itemId}`);
    return stock ? parseInt(stock) : null;
}

// Routes

app.get('/list_products', (req, res) => {
    res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId);
    const item = getItemById(itemId);
    if (!item) {
        res.json({ status: 'Product not found' });
        return;
    }
    const currentQuantity = await getCurrentReservedStockById(itemId) ?? item.initialAvailableQuantity;
    res.json({ ...item, currentQuantity });
});

app.get('/reserve_product/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId);
    const item = getItemById(itemId);
    if (!item) {
        res.json({ status: 'Product not found' });
        return;
    }
    const reservedStock = await getCurrentReservedStockById(itemId);
    const currentStock = reservedStock ?? item.initialAvailableQuantity;

    if (currentStock < 1) {
        res.json({ status: 'Not enough stock available', itemId });
        return;
    }

    await reserveStockById(itemId, currentStock - 1);
    res.json({ status: 'Reservation confirmed', itemId });
});

app.listen(PORT, () => {
    console.log(`API available on localhost port ${PORT}`);
});
