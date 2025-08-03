import api from "@/_services/_authservices";


const passwordReset = async (data) => {
  try {
    const response = await api.post('/account/password-reseting/', data, {
      headers: { 'Content-Type': 'application/json' }
    });
    return response.status === 200;  // Adaptez au code retour réel de votre API
  } catch (error) {
    console.error("Reset error:", error);
    return false;
  }
};

const verifyToken = async (token) => {
  try {
    const response = await api.post('/api/password-reset/verify-token/', token, {
      headers: { 'Content-Type': 'application/json' },
    });
    return response.status === 200;
    
  } catch (error) {
    return console.log(error);
  }
};

const updatePassword = async () => {

  try {

    const response = await api.post('/account/password-reset/confirm/', {
      headers: {'Content-Type': 'application/json'}
    });
    return response.status === 200;
  } catch(error) {
    console.log(error)
  }

}

export {passwordReset, verifyToken, updatePassword}; 