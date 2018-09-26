<template>
    <div class="login-form">
        <div class="login-select">
            <span :class="{notLoginTypeCss:form.loginType != 'phone'}" @click="form.loginType='phone'">手机号登录</span>
            <span>|</span>
            <span :class="{notLoginTypeCss:form.loginType != 'user'}" @click="form.loginType='user'">用户名登录</span>
        </div>
        <div v-if="form.loginType=='phone'" class="form-item">
            <el-form ref="phoneForm" :model="form">
                <el-form-item>
                    <el-select v-model="form.area" style="width:250px;">
                        <el-option v-for="area in phoneArea" :key="area.value"
                            :label="area.label" :value="area.value"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item>
                    <el-input v-model="form.phoneNum" placeholder="手机号" style="width:250px;"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-input v-model="form.password" placeholder="密码" style="width:250px;"></el-input>
                </el-form-item>
            </el-form>
        </div>
        <div v-else class="form-item">
            <el-form ref="userForm" :model="form">
                <el-form-item>
                    <el-input v-model="form.username" placeholder="用户名" style="width:250px;"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-input v-model="form.password" placeholder="密码" style="width:250px;"></el-input>
                </el-form-item>
            </el-form>
        </div>
        <div class="forget-password">
            <span>
                <el-checkbox v-model="form.isRemember">一个月内自动登录</el-checkbox>
            </span>
            <span style="margin-left:20px;">忘记密码?</span>
        </div>
    </div>
</template>

<script>
export default {
  name: "LoginForm",
  data() {
    return {
      phoneArea: this.$store.state.user.phoneArea,
      form: {
        loginType: "phone",
        area: 0,
        phoneNum: "",
        username: "",
        password: "",
        isRemember: true
      }
    };
  },
  methods: {}
};
</script>

<style scoped>
.login-form {
  height: 350px;
  font-size: 14px;
  margin: 30px;
}

.login-form .form-item {
  margin-top: 30px;
}
.login-select span {
  margin-left: 20px;
}

.notLoginTypeCss {
  color: rgb(171,182,210);
  cursor: pointer;
}
</style>


