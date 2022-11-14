import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    counter: 0,
  },
  getters: {
    counterDouble(state) {
      return state.
    },
  },
  mutations: {
  },
  actions: {
    
  },
  modules: {
  }
})


  data: function() {
    return {
      counter: 0,
    }
  },
  methods: {
    increase: function () {
      this.counter += 1
    },
    decrease: function () {
      this.counter -= 1
    },
  },
  computed: {
    counterDouble: function () {
      return this.counter * 2
    },
  },