<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated class="futuristic-header">
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <q-toolbar-title>
          Inventory System
        </q-toolbar-title>

        <div class="header-icons">
          <q-icon name="settings" size="24px" class="q-mr-md" />
          <q-icon name="notifications" size="24px" />
        </div>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      class="futuristic-drawer"
    >
      <q-list>
        <q-item-label header class="text-h6">
          Tools
        </q-item-label>

        <EssentialLink
          v-for="link in linksList"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer>

    <q-drawer
      v-model="rightDrawerOpen"
      side="right"
      bordered
      class="futuristic-drawer"
    >
      <q-list>
        <q-item-label header class="text-h6">
          System Status
        </q-item-label>
        <q-item>
          <q-item-section avatar>
            <q-icon name="memory" color="primary" />
          </q-item-section>
          <q-item-section>
            <q-item-label>CPU Usage</q-item-label>
            <q-item-label caption>45%</q-item-label>
          </q-item-section>
        </q-item>
        <q-item>
          <q-item-section avatar>
            <q-icon name="storage" color="primary" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Storage</q-item-label>
            <q-item-label caption>2.3 TB / 5 TB</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-drawer>

    <q-page-container class="futuristic-container">
      <router-view />
    </q-page-container>

    <q-footer elevated class="futuristic-footer">
      <q-toolbar>
        <q-toolbar-title>
          <div class="footer-icons">
            <q-icon name="speed" size="24px" class="q-mr-md" />
            <q-icon name="wifi" size="24px" class="q-mr-md" />
            <q-icon name="battery_full" size="24px" />
          </div>
        </q-toolbar-title>
        <div class="footer-status">
          <q-icon name="schedule" size="24px" class="q-mr-md" />
          <span>Last Updated: {{ currentTime }}</span>
        </div>
      </q-toolbar>
    </q-footer>
  </q-layout>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';
import EssentialLink, { EssentialLinkProps } from 'components/EssentialLink.vue';

defineOptions({
  name: 'MainLayout'
});

const leftDrawerOpen = ref(false);
const rightDrawerOpen = ref(true);
const currentTime = ref(new Date().toLocaleTimeString());

const updateTime = () => {
  currentTime.value = new Date().toLocaleTimeString();
};

onMounted(() => {
  const timer = setInterval(updateTime, 1000);
  onUnmounted(() => clearInterval(timer));
});

const linksList: EssentialLinkProps[] = [
  {
    title: 'Dashboard',
    caption: 'Main Overview',
    icon: 'dashboard',
    link: '/'
  },
  {
    title: 'Quick Links',
    caption: 'Navigation Menu',
    icon: 'link',
    link: '/links'
  },
  {
    title: 'Inventory',
    caption: 'Stock Management',
    icon: 'inventory_2',
    link: '#'
  },
  {
    title: 'Analytics',
    caption: 'System Reports',
    icon: 'analytics',
    link: '#'
  },
  {
    title: 'Settings',
    caption: 'System Configuration',
    icon: 'settings',
    link: '#'
  }
];

function toggleLeftDrawer () {
  leftDrawerOpen.value = !leftDrawerOpen.value;
}
</script>

<style lang="scss">
.futuristic-header {
  background: rgba(25, 118, 210, 0.8) !important;
  backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  
  .header-icons {
    color: white;
    .q-icon {
      animation: glow 2s infinite;
    }
  }
}

.futuristic-drawer {
  background: rgba(25, 118, 210, 0.1) !important;
  backdrop-filter: blur(10px);
  border-right: 1px solid rgba(255, 255, 255, 0.1);

  .q-item {
    transition: all 0.3s ease;
    
    &:hover {
      background: rgba(25, 118, 210, 0.2);
      transform: translateX(5px);
    }

    .q-icon {
      animation: pulse 2s infinite;
    }
  }
}

.futuristic-container {
  background: linear-gradient(135deg, rgba(25, 118, 210, 0.1) 0%, rgba(13, 71, 161, 0.1) 100%);
  backdrop-filter: blur(10px);
}

.futuristic-footer {
  background: rgba(25, 118, 210, 0.8) !important;
  backdrop-filter: blur(10px);
  border-top: 1px solid rgba(255, 255, 255, 0.1);

  .footer-icons {
    .q-icon {
      color: white;
      animation: glow 2s infinite;
    }
  }

  .footer-status {
    color: white;
    display: flex;
    align-items: center;
  }
}

@keyframes pulse {
  0% {
    opacity: 0.3;
    transform: scale(1);
  }
  50% {
    opacity: 0.6;
    transform: scale(1.2);
  }
  100% {
    opacity: 0.3;
    transform: scale(1);
  }
}

@keyframes glow {
  0% {
    text-shadow: 0 0 5px rgba(255, 255, 255, 0.5);
  }
  50% {
    text-shadow: 0 0 20px rgba(255, 255, 255, 0.8);
  }
  100% {
    text-shadow: 0 0 5px rgba(255, 255, 255, 0.5);
  }
}

.q-page-container {
  padding: 1rem;
}
</style>
