<template>
  <div id="app">
    <TodoList :todos="todos" @delete-todo="deleteTodo">
    <TodoForm :@create-todo="createTodo"/>
    <TodoForm/>
  </div>
</template>

<script>
import TodoForm from '@/components/TodoForm'
import TodoList from '@/components/TodoList'


export default {
  name: 'App',
  components: {
    TodoForm,
    TodoList,
  },
  data: function () {
    return {
      todos: [],
    }
  },
  methods: {
    createTodo: function (todoTitle) {
      const todo = {
        title: todoTitle
      }
      this.todos.push(todo)
    } 
  }
}
</script>

<style>

</style>
