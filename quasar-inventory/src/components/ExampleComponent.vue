<template>
  <div>
    <video ref="video" autoplay></video>
    <button @click="startCamera">Start Camera</button>
    <button @click="stopCamera">Stop Camera</button>
    <button @click="takePicture">Take Picture</button>
    <canvas ref="canvas" style="display: none;"></canvas>
    <div>The image is a {{ result }}</div>
  </div>
</template>

<script setup>
import { ref, onBeforeUnmount } from 'vue';
import { processImage } from '../api/main';

const video = ref(null);
let stream = null;
const canvas = ref(null);
const imageUrl = ref(null);
const result = ref(null);

const startCamera = async () => {
  try {
    stream = await navigator.mediaDevices.getUserMedia({ video: true });
    if (video.value) {
      video.value.srcObject = stream;
    }
  } catch (error) {
    console.error('Error accessing camera:', error);
  }
};

const stopCamera = () => {
  if (stream) {
    stream.getTracks().forEach(track => track.stop());
  }
};


const takePicture = async () => {
  if (!video.value || !canvas.value) return;

  const context = canvas.value.getContext('2d');
  canvas.value.width = video.value.videoWidth;
  canvas.value.height = video.value.videoHeight;

  context.drawImage(video.value, 0, 0, canvas.value.width, canvas.value.height);
  imageUrl.value = canvas.value.toDataURL('image/jpeg', 0.9); // Convert to base64 image


  imageUrl.value = imageUrl.value.split('data:image/jpeg;base64,')[1];

  const payload = {
    image_base64: imageUrl.value,
    question: 'What is in the image?'
  };
  result.value = await processImage(payload);
};

onBeforeUnmount(() => {
  stopCamera();
});
</script>

<style scoped>
video {
  width: 100%;
  max-width: 640px;
  border: 1px solid #ccc;
}
</style>