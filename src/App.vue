<script setup>
import { RouterLink, RouterView } from "vue-router";
import DrawerSidebar from "./views/DrawerSidebar.vue";
import BottomNavigation from "./views/BottomNavigation.vue";
</script>

<template>
    <DrawerSidebar />
  <div>
    <nav>
      </nav>
    </div>

  <RouterView />
  
  <BottomNavigation/>
</template>

<style scoped>

</style>
