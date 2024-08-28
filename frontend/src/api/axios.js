import axios from 'axios';

const axiosInstance = axios.create({
    baseURL: 'http://localhost:8000',  // Django backend
    headers: {
        'Content-Type': 'application/json',
    },
    withCredentials: true,  // This allows cookies to be sent along with the requests
});

export default axiosInstance;
