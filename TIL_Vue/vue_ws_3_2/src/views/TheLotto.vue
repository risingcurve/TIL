<template>
  <div class="lotto">
    <h1>로또</h1>
    <button @click="getLottoNums">Get Lucky Numbers</button>
    <div v-show="lottoNumbers">
      <p>{{ lottoNumbers }}</p>
      <button @click="goLunchPage">처음으로</button>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLotto',
  data () {
    return {
      lottoNumbers: null,
      lunchMenu: this.$route.params.lunchMenu,
    }
  },
  methods: {
    getLottoNums () {
      const numbers = _.range(1, 46)
      this.lottoNumbers = _.sampleSize(numbers, 6)
    },

    goLunchPage () {
      this.$router.push({
        name: 'lunch',
        params: { 
          lottoNumbers: this.lottoNumbers
        }
      })
    }
  }
}
</script>

<style>

</style>