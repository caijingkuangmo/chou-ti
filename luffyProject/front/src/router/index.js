import Vue from 'vue'
import Router from 'vue-router'
import LoginComponent from "@/components/login.vue"
import HomeComponent from "@/components/home/home.vue"
import CourseComponent from "@/components/course/course.vue"
import MicroComponent from "@/components/micro/micro.vue"
import NewsComponent from "@/components/news/news.vue"
import mainStore from "@/store/index.js"

Vue.use(Router)

const router = new Router({
    routes: [{
            path: '/',
            name: 'home',
            component: HomeComponent
        },
        {
            path: '/login',
            name: 'login',
            component: LoginComponent
        },
        {
            path: '/home',
            name: 'home',
            component: HomeComponent
        },
        {
            path: '/course',
            name: 'course',
            component: CourseComponent
        },
        {
            path: '/micro',
            name: 'micro',
            meta: { requiresAuth: true, },
            component: MicroComponent
        },
        {
            path: '/news',
            name: 'news',
            component: NewsComponent,
            meta: { requiresAuth: true, }
        },
    ]
})


router.beforeEach((to, from, next) => {
    if (to.meta.requiresAuth === false) {
        next()
    } else {
        if (mainStore.state.account.isLogin === true) {
            next()
        } else {
            next({
                path: '/login',
                query: {
                    redirect: to.fullPath
                }
            })
        }
    }
})


export default router;