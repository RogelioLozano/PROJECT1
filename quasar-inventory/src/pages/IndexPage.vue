<template>
  <q-page class="futuristic-page">
    <div class="content-container">
      <h1 class="text-h3 text-weight-thin text-center q-mb-xl">
        Inventory Scanner
      </h1>
      <div class="camera-container q-pa-md">
        <example-component></example-component>
      </div>
    </div>
  </q-page>
</template>

<script setup lang="ts">
import ExampleComponent from 'components/ExampleComponent.vue';

defineOptions({
  name: 'IndexPage'
});
</script>

<style lang="scss" scoped>
.futuristic-page {
  min-height: 100vh;
  background: linear-gradient(135deg, #1976D2 0%, #0D47A1 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

.content-container {
  width: 100%;
  max-width: 1200px;
  
  h1 {
    color: white;
    text-shadow: 0 2px 4px rgba(0,0,0,0.2);
  }
}

.camera-container {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border-radius: 20px;
  box-shadow: 0 8px 32px rgba(0,0,0,0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  
  :deep(video) {
    border-radius: 12px;
    box-shadow: 0 4px 16px rgba(0,0,0,0.2);
  }
  
  :deep(button) {
    margin: 1rem 0.5rem;
    background: rgba(255, 255, 255, 0.2);
    border: none;
    padding: 0.5rem 1rem;
    color: white;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.3s ease;
    
    &:hover {
      background: rgba(255, 255, 255, 0.3);
      transform: translateY(-2px);
    }
  }
  
  :deep(div) {
    color: white;
    margin-top: 1rem;
    font-size: 1.2rem;
  }
}
</style>
