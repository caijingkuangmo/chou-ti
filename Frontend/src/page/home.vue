<template>
    <div id="home">
        <div class="nav-bar">
            <NavBar></NavBar>
        </div>
        <div class="content-display-area">
            <ContentDisplayArea></ContentDisplayArea>
        </div>
    </div>
</template>

<script>
import NavBar from '@/components/nav/nav-bar.vue'
import ContentDisplayArea from '@/components/content/content-display-area.vue';

export default {
    name:'home',
    data () {
        return {

        }
    },
    methods: {

    },
    components:{
        ContentDisplayArea,
        NavBar
    }
}
</script>

<style scoped>

</style>


