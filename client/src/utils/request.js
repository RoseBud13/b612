import axios from "axios";

const oneApi = axios.create({
    baseURL: '/oneapi',
    timeout: 2000
});

export default oneApi;