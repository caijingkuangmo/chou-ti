<template>
    <div>
        <div>
            <el-col :span="6" v-for="(val, index) in li" :key="index" v-if="index % 3 == 0">{{val}}-{{index}}</el-col>
            <el-col :span="6" v-for="(val, index) in li" :key="index" v-if="index % 3 == 1">{{val}}-{{index}}</el-col>
            <el-col :span="6" v-for="(val, index) in li" :key="index" v-if="index % 3 == 2">{{val}}-{{index}}</el-col>
        </div>
    </div>
</template>

<script>
export default {
    name:"test",
    data () {
        return {
           li:[0,1,2,0,1,2,0,1,2,0,1,2] 
        }
    }
}
</script>
<style scoped>

</style>


