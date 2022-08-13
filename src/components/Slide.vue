<template>
  <div class="transition-transform drawer drawer-end">
      <div class="drawer-content">
          <!-- Page content here -->
    </div>
        <!-- <input id="my-drawer" type="checkbox" class="drawer-toggle" /> -->
    <div class="drawer-side">
      <label for="my-drawer" class="drawer-overlay"></label>
      <ul
        class="
          menu
          p-4
          overflow-y-auto
          h-screen
          w-screen
          bg-base-300
          text-base-content
        "
      >
        <!-- Sidebar content here -->
        <div></div>
        <li><a>Item 1</a></li>
        <li><a>Item 2</a></li>
        <li><a>Item 3</a></li>
        <li><a>Item 4</a></li>
        <li><a>Item 5</a></li>
        <li><a>Item 6</a></li>
      </ul>
    </div>
  </div>
</template>
<script>
export default {
  name: "Slide",
};
</script>