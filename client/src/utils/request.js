import axios from "axios";

const request = axios.create({
    baseURL: '/',
    // baseURL: 'http://v3.wufazhuce.com:8000/api',
    timeout: 5000
});

export default request;