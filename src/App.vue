<script setup>
import { RouterLink, RouterView } from "vue-router";
import DrawerSidebar from "./views/DrawerSidebar.vue";
import BottomNavigation from "./views/BottomNavigation.vue";
</script>

<template>
    <DrawerSidebar />
  <div>
    <nav>
      <RouterLink class="btn" to="/">Home</RouterLink>
        <RouterLink class="btn" to="/Search">Search</RouterLink>
        <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Et id, corporis nesciunt nobis consequuntur dolorem unde natus fugiat fugit dicta sapiente? Similique repellendus veniam a debitis ea fugit incidunt optio.</p>
      </nav>
    </div>
  <RouterView />
  
  <BottomNavigation/>
</template>

<style scoped>

</style>
