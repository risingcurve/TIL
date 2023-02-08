<template>

  <h1>2-1. 목록의 항목을 필터링할 때</h1>

  <!-- bad -->
  <!-- <ul>
    <li
      v-for="user in users"
      v-if="user.isActive"
      :key="user.id"
    >
      {{ user.name }}
    </li>
  </ul> -->



  <!-- good (1) -->
  <!-- <ul>
    <li
      v-for="user in activeUsers"
      :key="user.id"
    >
      {{ user.name }}
    </li>
  </ul> -->


  
  <!-- good (2) -->
  <!-- <ul>
    <template 
      v-for="user in users" 
      :key="user.id"
    >
      <li v-if="user.isActive">
        {{ user.name }}
      </li>
    </template>
  </ul> -->


</template>

<script>
  computed: {
    activeUsers() {
      return this.users.filter((user) => user.isActive)
      }
  }
</script>
