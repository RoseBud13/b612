import axios from "axios";
import { storage } from '../utils/storage'

const server = axios.create({
    // development mode
    baseURL: 'http://127.0.0.1:5000/',
    timeout: 5000
});

// Add a request interceptor
server.interceptors.request.use(
    config => {
        const token = storage.getAuthToken();
        if(token) {
            config.headers.Authorization = token;
        }
        return config;
    },
    error => {
        console.log(error);
        return Promise.reject();
    }
);

export default server;