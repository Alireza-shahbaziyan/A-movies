<template>
  <!-- slide box -->
  <div class="h-64 w-full">
    <swiper
      :spaceBetween="30"
      :centeredSlides="true"
      :autoplay="{ delay: 2500, disableOnInteraction: false }"
      :pagination="{ clickable: true }"
      :navigation="true"
      :modules="modules"
      class="mySwiper w-full h-full"
    >
      <!-- Slide -->
      <swiper-slide v-for="i in images" :key="i.id" class="text-center text-lg bg-white flex justify-center items-center">
        <img class="w-full h-full block" :src="i.image" alt="Image"/>
      </swiper-slide>
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
  name:"TopCarousel",
  components: {
    Swiper,
    SwiperSlide,
  },
  setup() {
    return {
      modules: [Autoplay, Pagination, Navigation],
    };
  },
  data() {
    return {
      images: [
        {
          id: 1,
          image:
            "https://m.media-amazon.com/images/M/MV5BZGNkMjUyOTMtZjk2Yy00NTExLWI2YWUtZDE4MTg5NjZiZjZkXkEyXkFqcGdeQXVyMDM2NDM2MQ@@._V1_.jpg",
        },
        {
          id: 2,
          image:
            "https://static1.colliderimages.com/wordpress/wp-content/uploads/2022/02/Shutter-Island-Ending-Explained.jpg",
        },
        {
          id: 3,
          image:
            "https://www.showbizgalore.com/wp-content/uploads/2022/06/dfdddd.jpg",
        },
        {
          id: 4,
          image:
            "https://images-na.ssl-images-amazon.com/images/S/pv-target-images/b92d2865829416e35e7102a3934a2ee745f3b903a95678710442d4299d86f39c._RI_.jpg",
        },
        {
          id: 5,
          image:
            "https://static1.colliderimages.com/wordpress/wp-content/uploads/2022/03/the-godfather-character-guide.jpg",
        },
      ],
    };
  },
};
</script>
