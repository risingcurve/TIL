import React from 'react'
import { useRecoilValue } from 'recoil'
import { filteredTodoListState } from './RecoilState'
import TodoItemCreator from './TodoItemCreator'
import TodoItem from './TodoItem'
import TodoListStats from './TodoListStats'
import TodoListFilters from './TodoListFilters'



export default function TodoList() {
  // const todoList = useRecoilValue(todoListState)
  const todoList = useRecoilValue(filteredTodoListState)

  return (
    <div>
      <TodoListStats />
      <TodoListFilters />
      <TodoItemCreator />

      {todoList.map((todoItem) => (
        <TodoItem key={todoItem.id} item={todoItem} />
      ))}
    </div>
  )
}