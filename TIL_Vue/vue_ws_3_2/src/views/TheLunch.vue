<template>
  <div class="lunch">
    <h1>점심메뉴</h1>
    <button @click="pickLunchMenu">Pick Lunch</button>
    <div v-show="lunchMenu">
      <p>{{ lunchMenu }}</p>
    </div>
    <br>
    <div>
      <h2>로또를 뽑아보자</h2>
      <button @click="goLottoPage">Pick Lotto</button>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLunch',
  data () {
    return {
      menus: ['짜장면', '짬뽕', '간짜장', '라면', '칼국수', '냉면'],
      lunchMenu: null,
    }
  },
  methods: {
    pickLunchMenu () {
      // console.log('Pick')
      this.lunchMenu = _.sample(this.menus)
    },

    goLottoPage () {
      // url을 통해 값을 전달하는 부분
      // this.$router.push(`/lotto/${this.lunchMenu}`)
      // 아래 방식을 권장
      // 요청(request) 을 보내는 부분
      this.$router.push({ 
        name: 'lotto', 
        params: { 
          lunchMenu: this.lunchMenu 
        }
      })
    }
  }
}
</script>

<style>

</style>