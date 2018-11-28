<template>
  <div style="position: relative;">
    <div style="width:100%; height:300px;background:yellow;"></div>
    <img :src="PlayJpg" alt="" style="display:block;height:65px;width:65px;position: absolute;left: 50px;top: 50px;">
  </div>
</template>

<script>
  import PlayJpg from "@/assets/play.png"
  export default {
    name: "test",
    data() {
      return {
        li: [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2],
        PlayJpg,
      }
    }
  }

</script>
<style scoped>
  .a {}

</style>
