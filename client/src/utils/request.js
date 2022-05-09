import axios from "axios";

const oneApi = axios.create({
    baseURL: 'http://v3.wufazhuce.com:8000/api',
    timeout: 2000
});

export default oneApi;