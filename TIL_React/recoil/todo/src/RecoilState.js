import { atom, selector } from 'recoil'

export const todoListState = atom({
  key: 'todoListState',
  default: [],
})
