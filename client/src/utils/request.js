import axios from "axios";

const oneApi = axios.create({
    baseURL: '/oneapi',
    // baseURL: 'http://v3.wufazhuce.com:8000/api',
    timeout: 5000
});

export default oneApi;