<template>
  <div>
    <Nav></Nav>
    <h1>micro</h1>
  </div>
</template>

<script>
  import Nav from "@/components/index.vue"
  export default {
    name: "micro",
    components: {
      Nav,
    },
    created() {
      console.log(this.$store.state.account.username);
      console.log(this.$store.state.account.token);
      console.log(this.$store.state.account.isLogin);

    },
    data() {
      return {

      }
    }
  }

</script>

<style scoped>

</style>
