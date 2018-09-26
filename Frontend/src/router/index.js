import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/page/home.vue'
import Boot from '@/page/boot.vue'

Vue.use(Router)

export default new Router({
    routes: [{
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/boot',
            name: 'boot',
            component: Boot
        }
    ]
})