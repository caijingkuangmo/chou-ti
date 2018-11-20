// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import VueRouter from "vue-router"
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import lang from "element-ui/lib/locale/lang/en"
import locale from "element-ui/lib/locale"
Vue.use(ElementUI)

import store from './store/index.js'
import routerConfig from "./router.config.js"

Vue.config.productionTip = false

Vue.use(VueRouter);

const router = new VueRouter(routerConfig);

/* eslint-disable no-new */
new Vue({
  store,
  el: '#app',
  components: { App },
  template: '<App/>',
  router
})
