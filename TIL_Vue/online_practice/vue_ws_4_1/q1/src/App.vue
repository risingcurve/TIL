<template>
  <div id="app">
    <h1> 버튼 박스 제작</h1>
    <div id="box">

      <h2>예약 페이지</h2>
      <div class="box">

        <h3> 시간 선택</h3>
        <div class="timelinebox">

          <div class="pick"  v-for="(time,index) in times" :key="index" v-on:click="selectTime">
              {{time}}
          </div>
        </div>
        <hr>
        <h3>선택한 시간 : {{selectedTimes.join(" ")}}</h3>
      </div>
      
      <!-- <h3>선택한 시간 {{selectedTimesString}}</h3> -->
    </div>
  </div>
</template>


<script>

export default {
  name: 'App',
  data: function (){
    return {
      times: [
      "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
    "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
    "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
      ],
      isSelected: false,
      selectedTimes:[],
      selectedTimesString: ''
    }
  },
  methods:{
    selectTime: function(event){
      console.log(this.selectedTimes);
      // if (event.target.classList.contains("selectedColor")){
        // event.target.classList.remove("selectedColor")
      //   }else{
        //     event.target.classList.add("selectedColor")
      //     }
         //색깔 바꾸기
      // 5개 이상 선택 못하게
      console.log(event.target.textContent);
      if (this.selectedTimes.includes(event.target.textContent)){
        this.selectedTimes.splice(this.selectedTimes.indexOf(event.target.textContent),1)
        event.target.classList.remove("selectedColor")

      }
      else{
        if (this.selectedTimes.length>=5){
          alert('5개 이상 선택 할수 없습니다.')
       }else{
         this.selectedTimes.push(event.target.textContent)
         event.target.classList.add("selectedColor")
       }
      }
      // console.log(event.target.textContent);
      // console.log("????,",this.selectedTimes);
      this.selectedTimesString = this.selectedTimes.toString(' ')
      // console.log(this.selectedTimesString);
    }
  }
  // 클릭 했을 때 색 변하게 하기, 카운트, 배열에 저장


}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
button{
  background: none;
  border: none;
}
.pick{

  margin: 2px;
  cursor: pointer;
  display: inline;
}
.sky-blue{
  background-color: #658dc63d;
}
.selectedColor{
  background: #658dc63d;
}
hr{
  width : 80%;
}
.box{
  width: 80%;
  margin: auto;
  border: solid
}
.timelinebox{
  margin:auto;
  width: 60%;
}
</style>