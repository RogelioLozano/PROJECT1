import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL;

export async function processImage(payload: object) {
    try {
        const response = await axios.post(API_URL, JSON.stringify(payload), {
            headers: {
                'Content-Type': 'application/json'
            }
        });
        return response.data.answer;
    } catch (error) {
        console.error('Error:', error);
    }
}
