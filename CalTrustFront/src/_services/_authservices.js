import axios from "axios";
import router from "../router"; // Importez votre router si nécessaire

const api = axios.create({
    baseURL: 'http://localhost:8000',
    timeout: 100000,
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
        
        // Si erreur 401 (Unauthorized) et ce n'est pas une requête de refresh
        if (error.response?.status === 401 && 
            !originalRequest._retry && 
            !originalRequest.url.includes('/account/token/refresh/')) {
            
            originalRequest._retry = true;
            const refreshToken = localStorage.getItem('userTokenRefresh');
            
            if (refreshToken) {
                try {

                    // Rafraîchir le token
                    const refreshResponse = await axios.post(
                        'http://localhost:8000/account/token/refresh/', 
                        { refresh: refreshToken }
                    );
                    
                    const newAccessToken = refreshResponse.data.access;
                    localStorage.setItem('userToken', newAccessToken);
                    
                    // Mettre à jour le header et relancer la requête originale
                    originalRequest.headers.Authorization = `Bearer ${newAccessToken}`;
                    return api(originalRequest);
                    
                } catch (refreshError) {
                    console.error('Refresh token failed:', refreshError);
                    // Déconnexion si le refresh échoue
                    localStorage.removeItem('userToken');
                    localStorage.removeItem('userTokenRefresh');
                    localStorage.removeItem('username');
                    router.push('/signin?session_expired=true');
                    return Promise.reject(refreshError);
                }
            } else {
                // Pas de refresh token disponible
                localStorage.removeItem('userToken');
                router.push('/signin');
            }
        }

        return Promise.reject(error);
    }
);

export default api;