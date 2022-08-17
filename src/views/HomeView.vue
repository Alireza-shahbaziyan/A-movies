<script setup>
import TopCarousel from "../components/Home/TopCarousel.vue";
import BodyCarousel from "../components/Home/BodyCarousel.vue";
</script>

<template>
  <div class="h-full flex flex-col justify-start">
    <div>
      <TopCarousel />
    </div>
    <div class="h-1/2 flex flex-col justify-evenly">
      <div>
        <div class="text-2xl m-3.5">جدید ترین فیلم ها:</div>
        <BodyCarousel />
      </div>
      <div>
        <div class="text-2xl m-3.5">پر بازدید ترین فیلم ها:</div>
        <BodyCarousel />
      </div>
    </div>
  </div>
</template>
