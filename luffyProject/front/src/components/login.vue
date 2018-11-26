<template>
    <div>
        <el-form :model="loginForm" :rules="loginRules">
            <el-form-item label="用户名" prop="username">
                <el-input v-model="loginForm.username"></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="password">
                <el-input v-model="loginForm.password" type="password"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="login">登录</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
export default {
  name: "login",
  data() {
    return {
      loginForm: {
        username: "",
        password: ""
      },
      loginRules:{
          username:[
              {required:true, message:"请输入用户名", trigger:'blur'}
          ],
          password:[
              {required:true, message:"请输入密码", trigger:'blur'}
          ]
      }
    };
  },
  methods: {
      async login(){
        const result = await this.$store.dispatch('account/login', this.loginForm); 
        if(result.state_code != 1000) {
            this.$message.error(result.msg);
        } else {
            let redirect = this.$route.query.redirect ? this.$route.query.redirect : "/";
            this.$router.push(redirect);
        }
      }
  }
};
</script>

<style scoped>
</style>


