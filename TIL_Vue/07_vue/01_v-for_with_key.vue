<template>
  
  <h1>1. v-for은 항상 key와 함께 사용하기</h1>

  <!-- bad -->
  <!-- <ul>
    <li v-for="todo in todos">
      {{ todo.text }}
    </li>
  </ul> -->

  
  <!-- good -->
  <!-- <ul>
    <li
      v-for="todo in todos"
      :key="todo.id"
    >
      {{ todo.text }}
    </li>
  </ul> -->

</template>

<script>
  // todos: [
  //   { id: 1, text: 'Learn to use v-for' },
  //   { id: 2, text: 'Learn to use key' }
  // ]
</script>
