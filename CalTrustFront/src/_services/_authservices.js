// src/plugins/axios.js
import axios from "axios";

const api = axios.create({
    baseURL: 'http://localhost:8000', // Or 'http://127.0.0.1:8000'
    timeout: 10000,
    headers: {
        'Content-Type': 'application/json', // Often good to explicitly set for POST
    }
});

export default api;