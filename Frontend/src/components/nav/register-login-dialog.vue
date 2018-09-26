<template>
    <div id="login-dialog">
      <el-dialog
        :visible="dialogVisible"
        width="770px"
        :show-close="false">
        <div>
          <div class="login">
            <div class="titles">登录</div>
            <LoginForm></LoginForm>
            <div class="buttons">
              <el-button @click="dialogVisible = false" type="primary">登录</el-button>
            </div>
          </div>
          <div class="register">
            <div class="titles">
              <span>注册</span>
              <el-button icon="el-icon-close" @click="closeDialog"></el-button>
            </div>
            <ReisterForm></ReisterForm>
            <div class="buttons">
              <el-button type="primary" @click="dialogVisible = false">下一步</el-button>
            </div>
          </div>
        </div>
      </el-dialog>
    </div>
</template>

<script>
import LoginForm from './login-form.vue'
import ReisterForm from './register-form.vue'

export default {
  name: "RegisterLoginDialog",
  data() {
    return {
      dialogVisible: false
    };
  },
  methods: {
    showDialog(){
      this.dialogVisible = true;
    },
    closeDialog(){
      this.dialogVisible = false;
    }
  },
  components:{
    LoginForm,
    ReisterForm
  }
};
</script>

<style>
#login-dialog .el-dialog__header{
  padding: 0 !important;
}
#login-dialog .el-dialog__body{
  padding: 0 !important;
  font-size:0;
}

.titles .el-button{
  padding: 0;
  margin: 0;
  background: rgb(231,236,242);
  margin-left:340px;
}
</style>


<style scoped>
.login{
  width:349px;
  display: inline-block;
  border-right:1px solid gray;
}

.register{
  width:420px;
  display: inline-block;
}

.titles{
  background:rgb(231,236,242);
  font-size:14px;
  padding: 12px 0 12px 20px;
}
#login-dialog .buttons{
  margin-top:-40px;
  margin-left: 110px;
  margin-bottom:20px;
}
</style>


