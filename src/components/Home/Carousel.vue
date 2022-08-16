<template>
  <div class="h-64	w-full">
<swiper
    :spaceBetween="30"
    :centeredSlides="true"
    :autoplay="{
      delay: 2500,
      disableOnInteraction: false,
    }"
    :pagination="{
      clickable: true,
    }"
    :navigation="true"
    :modules="modules"
    class="mySwiper w-full h-full"
  >
    <swiper-slide class="text-center	text-lg bg-white flex justify-center items-center"><img class="object-cover	w-full h-full block" src="../../assets/12AngrayMan.jpg" alt="image"></swiper-slide>
    <swiper-slide class="text-center	text-lg bg-white flex justify-center items-center"><img class="object-cover	w-full h-full block" src="../../assets/12AngrayMan.jpg" alt="image"></swiper-slide>
    <swiper-slide class="text-center	text-lg bg-white flex justify-center items-center"><img class="object-cover	w-full h-full block" src="../../assets/12AngrayMan.jpg" alt="image"></swiper-slide>
    <swiper-slide class="text-center	text-lg bg-white flex justify-center items-center"><img class="object-cover	w-full h-full block" src="../../assets/12AngrayMan.jpg" alt="image"></swiper-slide>
    <swiper-slide class="text-center	text-lg bg-white flex justify-center items-center"><img class="object-cover	w-full h-full block" src="../../assets/12AngrayMan.jpg" alt="image"></swiper-slide>
    <swiper-slide class="text-center	text-lg bg-white flex justify-center items-center"><img class="object-cover	w-full h-full block" src="../../assets/12AngrayMan.jpg" alt="image"></swiper-slide>
    <swiper-slide class="text-center	text-lg bg-white flex justify-center items-center"><img class="object-cover	w-full h-full block" src="../../assets/12AngrayMan.jpg" alt="image"></swiper-slide>
    <swiper-slide class="text-center	text-lg bg-white flex justify-center items-center"><img class="object-cover	w-full h-full block" src="../../assets/12AngrayMan.jpg" alt="image"></swiper-slide>
    <swiper-slide class="text-center	text-lg bg-white flex justify-center items-center"><img class="object-cover	w-full h-full block" src="../../assets/12AngrayMan.jpg" alt="image"></swiper-slide>
  </swiper>
  </div>
</template>
<script>
// Import Swiper Vue.js components
import { Swiper, SwiperSlide } from "swiper/vue";

// Import Swiper styles
import "swiper/css";

import "swiper/css/pagination";
import "swiper/css/navigation";

// import required modules
import { Autoplay, Pagination, Navigation } from "swiper";

export default {
  components: {
    Swiper,
    SwiperSlide,
  },
  setup() {
    return {
      modules: [Autoplay, Pagination, Navigation],
    };
  },
};
</script>
<style scoped>
.swiper-slide {

  /* Center slide text vertically */
  display: -webkit-box;
  display: -ms-flexbox;
  display: -webkit-flex;
  /* display: flex; */
  -webkit-box-pack: center;
  -ms-flex-pack: center;
  -webkit-justify-content: center;
  /* justify-content: center; */
  -webkit-box-align: center;
  -ms-flex-align: center;
  -webkit-align-items: center;
  /* align-items: center; */
}
</style>
<!-- sliders: [
        {
          slide: "https://picsum.photos/200/300",
        },
        {
          slide: "https://picsum.photos/200",
        },
        {
          slide: "https://picsum.photos/id/237/200/300",
        },
        {
          slide: "https://picsum.photos/seed/picsum/200/300",
        },
      ], -->