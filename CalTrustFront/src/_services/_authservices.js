import axios from "axios";
import router from "../router"; // Importez votre router si nécessaire

const api = axios.create({
    baseURL: 'http://localhost:8000',
    timeout: 100000,
    headers: {
        'Content-Type': 'application/json',
    },
    withCredentials: true // Activé globalement si vous utilisez des cookies
});

api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('userToken');
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

api.interceptors.response.use(
    (response) => response,
    async (error) => {
        const originalRequest = error.config;
        
        // Cas spécifique du 403 + éviter les boucles infinies
        if (error.response?.status === 403 && !originalRequest._retry) {
            originalRequest._retry = true;

            try {
                const refreshResponse = await api.post('/account/token/refresh/');
                const newAccessToken = refreshResponse.data.access;
                
                localStorage.setItem('userToken', newAccessToken);
                originalRequest.headers.Authorization = `Bearer ${newAccessToken}`;
                
                return api(originalRequest); // Utilisez 'api' et non 'axiosInstance'
            } catch (refreshError) {
                // Cleanup et redirection si le refresh échoue
                localStorage.removeItem('userToken');
                router.push('/signin?session_expired=true');
                return Promise.reject(refreshError);
            }
        }

        // Gestion d'autres erreurs communes
        if (error.response?.status === 401) {
            localStorage.removeItem('userToken');
            router.push('/signin');
        }

        return Promise.reject(error);
    }
);

export default api;