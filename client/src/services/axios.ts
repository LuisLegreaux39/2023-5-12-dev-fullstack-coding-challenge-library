import axios from 'axios';
console.log(import.meta.env.VITE_SERVER_HOST as string)
const fetcher = axios.create({
    baseURL: import.meta.env.VITE_SERVER_HOST as string
});

export default fetcher