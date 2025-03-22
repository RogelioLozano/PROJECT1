f<template>
  <q-page class="links-page">
    <div class="content-container">
        <h1>Quick Links</h1>
    </div>
  </q-page>
</template>

<script setup lang="ts">
    
</script>

<style lang="scss" scoped>
.links-page {
  min-height: 100vh;
  background: linear-gradient(135deg, rgba(25, 118, 210, 0.1) 0%, rgba(13, 71, 161, 0.1) 100%);
  padding: 2rem;
}

.content-container {
  max-width: 1200px;
  margin: 0 auto;
  
  h1 {
    color: white;
    text-shadow: 0 2px 4px rgba(0,0,0,0.2);
  }
}

.links-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
  padding: 1rem;
}

.link-card {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border-radius: 16px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  transition: all 0.3s ease;
  overflow: hidden;
  
  &:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    background: rgba(255, 255, 255, 0.15);
  }
}

.link-item {
  :deep(.q-item) {
    padding: 1.5rem;
    color: white;
    
    &:hover {
      background: rgba(255, 255, 255, 0.1);
    }
  }
  
  :deep(.q-icon) {
    font-size: 2rem;
    color: rgba(255, 255, 255, 0.8);
    margin-right: 1rem;
    transition: all 0.3s ease;
  }
  
  :deep(.q-item__label) {
    font-size: 1.2rem;
    font-weight: 500;
  }
  
  :deep(.q-item__label--caption) {
    color: rgba(255, 255, 255, 0.7);
    font-size: 0.9rem;
  }
}
</style> 