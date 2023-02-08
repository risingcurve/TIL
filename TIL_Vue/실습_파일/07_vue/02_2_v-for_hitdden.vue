<template>

  <h1>2-2. 숨김 목록의 렌더링을 피할 때</h1>

  <!-- bad -->
  <!-- <ul>
    <li
      v-for="user in users"
      v-if="shouldShowUsers"
      :key="user.id"
    >
      {{ user.name }}
    </li>
  </ul> -->



  <!-- good -->
  <!-- <ul v-if="shouldShowUsers">
    <li
      v-for="user in users"
      :key="user.id"
    >
      {{ user.name }}
    </li>
  </ul> -->


</template>

<script>
  
</script>
