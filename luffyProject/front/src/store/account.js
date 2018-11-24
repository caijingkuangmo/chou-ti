import config from "@/config/config.js"
import axios from "axios"
import Cookie from "vue-cookies"


const state = {
  username: Cookie.get("username"),
  token: Cookie.get("token"),
  isLogin: Cookie.get("isLogin"),
}

var getters = {
  count(state) {
    return state.count;
  }
}

const mutations = {
  login(state, data) {
    state.username = data.username;
    state.token = data.token;
    Cookie.set("username", data.username, "20min");
    Cookie.set("token", data.token, "20min");
    state.isLogin = data.isLogin;
    Cookie.set("isLogin", data.isLogin, "20min");
  },
  logout(state) {
    state.username = "";
    state.token = "";
    state.isLogin = false;
    Cookie.remove("username");
    Cookie.remove("token");
    Cookie.remove("isLogin");
  }
}

const actions = {
  increment({
    commit,
    state
  }) {
    commit("increment");
  },
  async login({
    commit,
    state
  }, loginForm) {
    try {
      const resp = await axios.post(config.prefix + '/login/', loginForm);
      if (resp.data.state_code == 1000) {
        console.log('enter')
        commit('login', {
          token: resp.data.token,
          username: loginForm.name,
          isLogin: true
        });
      } else {
        commit('login', {})
      }
      return resp.data
    } catch (e) {
      console.log(e);
      commit('login', {})
      return {}
    }


  },
  async logout({
    commit,
    state
  }) {
    const resp = await axios.post(config.prefix + '/logout/');
    console.log(resp);
    commit('logout');
  }
}


export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
