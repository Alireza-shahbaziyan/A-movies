<script>
import NavbarView from "@/components/NavbarView.vue";
import Slide from "@/components/Slide.vue";
export default {
  name: "DrawerSidebar",
  components: {
    NavbarView,
    Slide
  },
  data() {
    return {
        showSlide:true
    }
  },
};
</script>
<!-- template -->
<template>
        <NavbarView @click="showSlide = !showSlide"/>
        <Slide :class="showSlide?'block':'hidden'"/>    
</template>
