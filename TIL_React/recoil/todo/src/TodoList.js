import React from 'react'
import { useRecoilValue } from 'recoil'
import { todoListState } from './RecoilState'
import TodoItemCreator from './TodoItemCreator'
import TodoItem from './TodoItem'
import TodoListStats from './TodoListStats'
import TodoListFilters from './TodoListFilters'



function TodoList() {
  const todoList = useRecoilValue(todoListState)

  return (
    <div>
      {/* <TodoListStats /> */}
      {/* <TodoListFilters /> */}
      <TodoItemCreator />

      {todoList.map((todoItem) => (
        <TodoItem key={todoItem.id} item={todoItem} />
      ))}
    </div>
  )
}