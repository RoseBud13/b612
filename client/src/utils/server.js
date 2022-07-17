import axios from "axios";

const server = axios.create({
    // development mode
    baseURL: 'http://127.0.0.1:5000/',
    timeout: 5000
});

export default server;