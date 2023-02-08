// App.vue

<template>
  <div id="app">
    <p>Counter: {{ counter }}</p>
    <p>Counter x2: {{ counterDouble }}</p>
    <p></p>
    <button @click="increase">increase +</button>
    <button @click="decrease">decrease -</button>
  </div>
</template>

<script>
export default {
  name: 'App', 
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
}
</script>

<style>
</style>