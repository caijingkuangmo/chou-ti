<template>
    <div class="container">
        <iframe class="nine" src="/boot" @load="get" ref="bokeyuan" frameborder="0"></iframe>
        <el-button @click="forward">前进</el-button>
        <el-button @click="backoff">后退</el-button>
        <el-button @click="redirect">跳转</el-button>
        <div class="dropdown">
            <button class="btn btn-default dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
                Dropdown
                <span class="caret"></span>
            </button>
            <ul class="dropdown-menu" aria-labelledby="dropdownMenu1">
                <li><a href="#">Action</a></li>
                <li><a href="#">Another action</a></li>
                <li><a href="#">Something else here</a></li>
                <li role="separator" class="divider"></li>
                <li><a href="#">Separated link</a></li>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
    name:'Boot',
    data () {
        return {
            
        }
    },
    mounted(){
        
    },
    methods: {
        forward(){
            this.$router.go(-1);
        },
        backoff(){
            this.$router.go(1);
        },
        redirect(){
            this.$router.push('/');
        },
        get(){
            // console.log(this.$refs.bokeyuan);
            console.log("589599",document.getElementsByClassName("nine")[0])
            console.log(document.getElementsByClassName("nine")[0].getElementsByTagName("html"))
        }
    }

}
</script>

<style scoped>
div{
    background: #eee;
    border:solid gray 1px;
}
</style>


