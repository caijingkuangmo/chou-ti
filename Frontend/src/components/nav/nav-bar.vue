<template>
    <div id="nav">
        <div class='logo'></div>
        <el-menu
            :default-active="activeIndex"
            class="menu"
            mode="horizontal"
            @select="handleSelect"
            background-color="rgb(36, 89, 162)"
            text-color="#fff"
            active-text-color="#ffd04b">
            <el-menu-item index="1">全部</el-menu-item>
            <el-menu-item index="2">42区</el-menu-item>
            <el-menu-item index="3">段子</el-menu-item>
            <el-menu-item index="4">图片</el-menu-item>
            <el-menu-item index="5">挨踢1024</el-menu-item>
            <el-menu-item index="6">你问我答</el-menu-item>
        </el-menu>
        <div class="nav-buttons" @click="showLoginDialog">
            <span @click="register">注册</span>
            <span id="login" @click="login">登录</span>
        </div>
        <div class="search-box">
            <div>
                <el-input></el-input>
            </div>
            <div class="search-icon">
                <el-button icon="el-icon-search" @click="search"></el-button>
            </div>
        </div>

        <RegisterLoginDialog ref="loginDialog"></RegisterLoginDialog>
    </div>
</template>

<script>
import RegisterLoginDialog from "./register-login-dialog.vue";

export default {
  name: "NavBar",
  data() {
    return {
      activeIndex: "1"
    };
  },
  components: {
    RegisterLoginDialog
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },
    search() {
      console.log("search");
    },
    register() {
      console.log("register");
    },
    login() {
      console.log("login");
    },
    showLoginDialog() {
      this.$refs["loginDialog"].showDialog();
    }
  }
};
</script>

<style scoped>
#nav {
  position: relative;
}

#nav ul {
  box-sizing: content-box;
}

#nav .logo {
  width: 20%;
  height: 23px;
  background: url("./../../assets/logo.png") no-repeat 0 0;
  position: absolute;
  z-index: 1;
  top: 20px;
  left: 1%;
}

.menu {
  padding-left: 20%;
  padding-right: 30%;
  width: 50%;
}

.nav-buttons {
  font-size: 14px;
  cursor: pointer;
  position: absolute;
  color: aliceblue;
  top: 20px;
  right: 25%;
}

#login {
  margin-left: 50px;
}

.search-box {
  position: absolute;
  right: 1%;
  top: 12px;
}

.search-box div {
  display: inline-block;
}

.search-icon {
  margin-left: -4px;
}
</style>


