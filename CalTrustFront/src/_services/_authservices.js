import { config } from "@vue/test-utils";
import axios from "axios";

const apiClient = axios.create({
    baseURL: 'http://localhost:8000/api/',
    withCredentials: true,
});

let accesToken = null;
let isRefreshing = false;
let failedQueue = [];