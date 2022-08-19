<script setup>
import TopCarousel from "../components/Home/TopCarousel.vue";
import BodyCarousel from "../components/Home/BodyCarousel.vue";
</script>

<template>
  <div class="h-full flex flex-col justify-start">
    <div class="h-1/3">
      <TopCarousel />
    </div>
    <div class="h-1/2 flex my-8 flex-col justify-evenly">
      <div>
        <div class="text-xl text-blue-500	 m-3.5">جدید ترین فیلم ها:</div>
        <BodyCarousel />
      </div>
      <div>
        <div class="text-xl text-blue-500	 m-3.5">پر بازدید ترین فیلم ها:</div>
        <BodyCarousel />
      </div>
    </div>
  </div>
</template>
