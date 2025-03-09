import axios from 'axios';

export async function processImage(payload: object) {
    try {
        const response = await axios.post('http://127.0.0.1:8000/vqa', JSON.stringify(payload), {
            headers: {
                'Content-Type': 'application/json'
            }
        });
        return response.data.answer;
    } catch (error) {
        console.error('Error:', error);
    }
}
