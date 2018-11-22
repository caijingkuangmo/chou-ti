<template>
    <div class="nav-line">
      <div class="logo">假装有图标</div>
      <div class="nav">
        <router-link to="/home">首页</router-link>
        <router-link to="/course">课程</router-link>
        <router-link to="/micro">微职位</router-link>
        <router-link to="/news">深科技</router-link>
      </div>
      <div class="login">
        <el-button @click="login">登录</el-button>
        <el-button>注册</el-button>
      </div>
    </div>
</template>

<script>
export default {
  name: "index",
  data() {
    return {};
  },
  methods: {
    login() {
      this.$router.push({ name: "login" });
    }
  }
};
</script>

<style scoped>
.nav-line .logo {
  display: inline-block;
  margin-left: 20px;
}

.nav-line .nav {
  display: inline-block;
  margin-left: 50px;
}

.nav-line .login {
  display: inline-block;
  margin-left: 50px;
}

.nav-line {
  line-height: 50px;
  height: 50px;
  padding: 5px 8px;
  background: #eee;
}
</style>


