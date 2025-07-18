// src/plugins/axios.js
import axios from "axios";
import { ref } from "vue";

const api = axios.create({
    baseURL: 'http://localhost:8000', // Or 'http://127.0.0.1:8000'
    timeout: 10000,
    headers: {
        'Content-Type': 'application/json', // Often good to explicitly set for POST
    }
});

const user = ref({
    username: "",
    email: "",
    password:"",
    user_type:"customer",
    phone:"",
    birth_date:null
})

const company = ref ({
    user_type : "firm",
    username : "",
    email: "",
    password: "",
    company_name: "",
    company_category: "",
    siret: "12345678901234",
    adress: ""

})

export default api;
export {user, company};
