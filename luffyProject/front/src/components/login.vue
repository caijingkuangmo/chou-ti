<template>
    <div>
        <el-form :model="loginForm" :rules="loginRules">
            <el-form-item label="用户名" prop="name">
                <el-input v-model="loginForm.name"></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="pwd">
                <el-input v-model="loginForm.pwd"></el-input>
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
        name: "",
        pwd: ""
      },
      loginRules:{
          name:[
              {required:true, message:"请输入用户名", trigger:'blur'}
          ],
          pwd:[
              {required:true, message:"请输入密码", trigger:'blur'}
          ]
      }
    };
  },
  methods: {
      async login(){
        const result = await this.$store.dispatch('account/login', this.loginForm); 
        if(result.state_code != 1000) {
            this.$message.error(result.message);
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


