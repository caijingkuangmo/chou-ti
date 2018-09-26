<template>
    <div class="register-form">
        <div>
            <el-steps :space="200" :active="0" finish-status="success">
                <el-step title="填写手机号"></el-step>
                <el-step title="填写基本资料"></el-step>
            </el-steps>
        </div>
        <div class="form-item">
            <el-form ref="registerForm" :model="form" v-if="activeStep==0">
                <el-form-item>
                    <el-select v-model="form.area" style="width:250px;">
                        <el-option v-for="area in phoneArea" :key="area.value"
                            :label="area.label" :value="area.value"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item>
                    <el-input v-model="form.phoneNum" placeholder="手机号" style="width:150px;">></el-input>
                    <el-button type="primary" style="width:100px;">获取验证码</el-button>
                </el-form-item>
                <el-form-item>
                    <el-input v-model="form.validCode" placeholder="验证码" style="width:250px;"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-input v-model="form.password" placeholder="密码" style="width:250px;"></el-input>
                </el-form-item>
            </el-form>

            <el-form ref="registerForm" :model="form" v-else>
                <!-- <el-form-item>
                    <el-select v-model="form.area">
                        <el-option v-for="area in phoneArea" :key="area.value"
                            :label="area.label" :value="area.value"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item>
                    <el-input v-model="form.phoneNum" placeholder="手机号"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-input v-model="form.password" placeholder="密码"></el-input>
                </el-form-item> -->
            </el-form>
        </div>
    </div>
</template>

<script>
export default {
  name: "RegisterForm",
  data() {
    return {
      activeStep: 0,
      phoneArea: this.$store.state.user.phoneArea,
      form: {
        area: 0,
        phoneNum: "",
        validCode: "",
        password: ""
      }
    };
  },
  methods: {}
};
</script>

<style scoped>
.register-form {
  height: 350px;
  font-size: 14px;
    margin:30px;
}
.register-form .form-item{
    margin-top:30px;
}
</style>

